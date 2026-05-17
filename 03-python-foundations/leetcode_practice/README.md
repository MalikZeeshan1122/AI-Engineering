# LeetCode-style Python practice (beginner → advanced)

This folder is **algorithm practice**, separate from the Jupyter curriculum in [`../exercises/`](../exercises/). Same topics appear on coding platforms (two pointers, heaps, DP); wording here is original so you drill **patterns**, not proprietary statements.

---

## Folder layout

| Path | Purpose |
|------|---------|
| **`problems/easy.py`** | Function stubs (`NotImplementedError`) — **you edit here**. |
| **`problems/medium.py`** | Medium-tier stubs — **you edit here**. |
| **`problems/hard.py`** | Harder stubs — **you edit here**. |
| **`solutions/easy.py`** | Reference implementations — peek **after** attempting the stub. |
| **`solutions/medium.py`** | Same for medium. |
| **`solutions/hard.py`** | Same for hard. |
| **`tests/checks_easy.py`** (etc.) | Shared assertion helpers—single suite per tier. |
| **`tests/test_student_*.py`** | Imports **`problems/`** — fails until you implement. |
| **`tests/test_reference_*.py`** | Imports **`solutions/`** — should always pass (sanity check). |

Imports assume your shell **current working directory** includes **`03-python-foundations`** as the package root (`leetcode_practice` is a package).

---

## How to practice

1. Implement functions in **`problems/easy.py`** (then medium, hard).
2. Run **student** tests from **`03-python-foundations`**:

```bash
cd 03-python-foundations
python -m unittest discover -s leetcode_practice/tests -p "test_student*.py" -v
```

3. Compare with **`solutions/`** only after an honest attempt.
4. Optionally verify references still match tests:

```bash
cd 03-python-foundations
python -m unittest discover -s leetcode_practice/tests -p "test_reference*.py" -v
```

**Dependencies:** stdlib only.

---

## Problem list

| Tier | Function | Idea |
|------|----------|------|
| Easy | `two_sum` | Hash map complement |
| Easy | `is_valid_parentheses` | Stack |
| Easy | `merge_sorted_lists` | Two pointers |
| Easy | `max_subarray_sum` | Kadane |
| Easy | `max_profit_one_transaction` | Track minimum price |
| Easy | `contains_duplicate` | Set membership |
| Easy | `is_anagram` | Character counts |
| Easy | `binary_search` | Halve search space |
| Easy | `single_number_xor` | XOR cancel pairs |
| Easy | `climb_stairs` | Fibonacci-style DP |
| Medium | `group_anagrams` | Bucket by sorted letters |
| Medium | `product_except_self` | Prefix / suffix products |
| Medium | `longest_unique_substring` | Sliding window (no repeats) |
| Medium | `top_k_frequent` | Count + heap / buckets |
| Medium | `search_in_rotated_sorted` | Modified binary search |
| Medium | `coin_change_min_coins` | Unbounded DP |
| Hard | `trap_rain_water` | Two pointers / levels |
| Hard | `word_break` | DP over prefixes |
| Hard | `merge_k_sorted_lists` | K-way merge (heap) |

---

## Map to curriculum notebooks

| Practice topic | See also (`exercises/`) |
|----------------|-------------------------|
| Lists, loops, dicts | `02`, `03`, `11` |
| Two pointers / windows | `02`, `07`, `11` |
| Stacks / queues | `06`, `18` |
| Sorting / bisect mindset | `03`, `11` |
| DP / recursion-shaped loops | `03`, `07` |
| Classes (if you extend locally) | `05`, [`../oop/`](../oop/README.md) |

---

## Note on originality

Ideas match widely taught interview topics; descriptions here are concise and independently phrased.
