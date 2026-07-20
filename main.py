import os
import csv
from collections import defaultdict, OrderedDict
from typing import Dict, Tuple, List
import html

from operator_groups import get_operator_profiles, resolve_operator_profile


# ====================== УТИЛИТЫ ======================
def normalize(s: str) -> str:
    return html.unescape((s or "").strip()).casefold()


def find_bucket_and_key(
    error_groups: "OrderedDict[str, OrderedDict[str, List[str]]]",
    text_norm: str
) -> Tuple[str, str]:
    for group_name, group_map in error_groups.items():
        for short_key, patterns in group_map.items():
            for p in patterns:
                if normalize(p) in text_norm:
                    return group_name, short_key
    return None, None


def read_csv_rows(path: str) -> List[Tuple[str, int]]:
    """
    Читает CSV и возвращает [(text, count), ...].
    Первая строка файла ВСЕГДА игнорируется (считаем её заголовком).
    Ожидается: первая колонка — текст ошибки, вторая — количество (или пусто -> 1).
    """
    rows: List[Tuple[str, int]] = []
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # пропускаем заголовок без условий
        next(reader, None)

        for row in reader:
            if not row:
                continue
            text = (row[0] or "").strip()
            if not text:
                continue
            try:
                count = int(row[1])
            except Exception:
                count = 1
            rows.append((text, count))
    return rows


# ====================== ОСНОВНАЯ ЛОГИКА ======================
def process_errors(
    error_groups: "OrderedDict[str, OrderedDict[str, List[str]]]",
    rows: List[Tuple[str, int]]
):
    """
    Возвращает:
      counters[group][short_key] = count,
      unclassified[label] = count,
      group_totals[group] = total_in_group,
      overall_total
    """
    counters: Dict[str, defaultdict] = {g: defaultdict(int) for g in error_groups.keys()}
    unclassified: defaultdict = defaultdict(int)

    for text, count in rows:
        g, k = find_bucket_and_key(error_groups, normalize(text))
        if g is None:
            if ": " in text:
                normalized_tail = ": ".join(text.split(": ")[-3:])
            else:
                normalized_tail = text
            label = "Ошибка искусственная: " + normalized_tail
            unclassified[label] += count
        else:
            counters[g][k] += count

    group_totals = OrderedDict()
    for group_name in error_groups.keys():
        group_totals[group_name] = sum(counters[group_name].values())
    if unclassified:
        group_totals["UNCLASSIFIED"] = sum(unclassified.values())

    overall_total = sum(group_totals.values())
    return counters, unclassified, group_totals, overall_total


def _merged_group_totals_for_summary(group_totals: "OrderedDict[str, int]") -> "OrderedDict[str, int]":
    """
    Для блока 'СВОД ПО ГРУППАМ' объединяем:
      'Unsuccessful Prebook' + 'Dynamic Errors' -> 'Prebook + Dynamic Errors'
    Остальные группы выводим как есть и в исходном порядке.
    """
    prebook_key = "Unsuccessful Prebook"
    dynamic_key = "Dynamic Errors"
    merged_label = "Prebook Errors"

    pre = group_totals.get(prebook_key, 0)
    dyn = group_totals.get(dynamic_key, 0)
    merged_value = pre + dyn

    out = OrderedDict()
    merged_done = False

    for k, v in group_totals.items():
        if k == prebook_key or k == dynamic_key:
            if not merged_done:
                out[merged_label] = merged_value
                merged_done = True
            continue
        out[k] = v

    return out


def print_detailed_tables(counters, unclassified, group_totals, overall_total):
    for group_name, group_counts in counters.items():
        if not group_counts:
            continue
        print(f"# {group_name}")
        for key, value in sorted(group_counts.items(), key=lambda x: (-x[1], x[0])):
            # print(f"- {key} - {value} шт")
            print(f"{key}\t{value}")
        print()

    if unclassified:
        print("# UNCLASSIFIED")
        for key, value in sorted(unclassified.items(), key=lambda x: (-x[1], x[0])):
            print(f"- {key} - {value} шт")
        print()

    print("# СВОД ПО ГРУППАМ")
    merged_totals = _merged_group_totals_for_summary(group_totals)

    for g, v in merged_totals.items():
        part = (v / overall_total * 100) if overall_total else 0.0
        print(f"- {g}: {v} шт ({part:.1f}%)")

    print(f"ИТОГО: {overall_total} шт\n")

# ====================== CLI ======================
def main():
    profiles = get_operator_profiles()
    print("Кого считаем?")
    for code, (title, _) in profiles.items():
        print(f"  {code} — {title}")
    while True:
        choice = input("Введи id или название оператора: ").strip()
        profile_title, profile_factory = resolve_operator_profile(choice)
        if profile_factory is not None:
            break
        available = ", ".join(profiles.keys())
        print(f"Некорректный ввод. Доступные id: {available}.")

    error_groups = profile_factory()

    default_path = "Edit visualization.csv"
    user_path = input(f"Путь к CSV [{default_path}]: ").strip() or default_path
    if not os.path.exists(user_path):
        raise FileNotFoundError(f"Файл не найден: {user_path}")

    print(f"Профиль: {profile_title}")
    print("------------------------------------------")

    rows = read_csv_rows(user_path)

    # raw_total = sum(count for _, count in rows)
    # print(f"Всего записей по данным CSV: {raw_total}")

    counters, unclassified, group_totals, overall_total = process_errors(error_groups, rows)
    print_detailed_tables(counters, unclassified, group_totals, overall_total)


if __name__ == "__main__":
    main()
