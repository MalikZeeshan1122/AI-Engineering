# LeetCode-style Python practice (beginner → advanced)

Classic interview patterns implemented **in plain Python** — complements the guided notebooks in [`../exercises/`](../exercises/) (syntax → asyncio → NumPy → HTTP).

## How to practice

1. Open [`problems/easy.py`](problems/easy.py), [`problems/medium.py`](problems/medium.py), and [`problems/hard.py`](problems/hard.py). Each function **`raise`s `NotImplementedError`** until you fill it in.
2. Run the **student** tests from the repo folder **`03-python-foundations`** (so imports resolve):

```bash
cd 03-python-foundations
python -m unittest discover -s leetcode_practice/tests -p "test_student*.py" -v
```

3. When stuck, peek at matching files in [`solutions/`](solutions/) **after** you try — muscle memory beats copy-paste.

4. Verify the **reference implementations** still pass (maintainers / sanity check):

```bash
cd 03-python-foundations
python -m unittest discover -s leetcode_practice/tests -p "test_reference*.py" -v
```

No extra packages required (stdlib only).

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

## Map to curriculum notebooks

| Practice topic | See also (`exercises/`) |
|----------------|----------------------|
| Lists, loops, dicts | `02`, `03`, `11` |
| Two pointers / windows | `02`, `07`, `11` |
| Stacks / queues | `06`, `18` |
| Sorting / bisect mindset | `03`, `11` |
| DP recursion patterns | `03`, `07` |
| Classes (if you extend problems) | `05`, `oop/` |

## Note on originality

Problem **ideas** are widely known (LeetCode / interview canon). Descriptions here are short and original phrasing is used so you can practice **patterns**, not scrape proprietary statements.
