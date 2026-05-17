#!/usr/bin/env python3
"""Generate OOP-focused notebooks with daily-life analogies. Run from 03-python-foundations/: python oop/build_oop_notebooks.py"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

OUT_DIR = Path(__file__).resolve().parent

NB_BASE: dict[str, Any] = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3", "version": "3.11.0"},
    },
}


def cell_md(text: str) -> dict[str, Any]:
    if not text.endswith("\n"):
        text += "\n"
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(True)}


def cell_code(text: str) -> dict[str, Any]:
    if not text.endswith("\n"):
        text += "\n"
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text.splitlines(True)}


def solution_md(title: str, code: str) -> dict[str, Any]:
    return cell_md(
        f"### Solution — {title}\n\n<details>\n<summary>Reveal solution</summary>\n\n```python\n{code.strip()}\n```\n\n</details>\n"
    )


def write_nb(name: str, cells: list[dict[str, Any]]) -> None:
    path = OUT_DIR / name
    nb = dict(NB_BASE)
    nb["cells"] = cells
    path.write_text(json.dumps(nb, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Wrote", path.name)


def banner(nb: str, title: str, level: str, prereq: str, nxt: str, analogies: str, objectives: list[str], toc: list[str]) -> list[dict[str, Any]]:
    objs = "\n".join(f"- {o}" for o in objectives)
    lines = "\n".join(f"{i + 1}. **{t}**" for i, t in enumerate(toc))
    md = f"""# Notebook {nb} — {title}

| | |
|---|---|
| **Focus** | Object-oriented Python ({level}) |
| **Daily-life theme** | {analogies} |
| **Pattern** | Story → Concept → Demo → **Exercise** → Solution |

**Prerequisites:** {prereq}

**Next notebook:** {nxt}

---

## Learning objectives

{objs}

## Table of contents

{lines}

---

> **Tip:** When an analogy clicks, rename classes to AI-flavored names (`Embedder`, `ToolRegistry`) — same mechanics.

---
"""
    return [cell_md(md)]


def nb_beginner() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "OOP-1",
            "Blueprints, alarms & coffee — instances in plain English",
            "Beginner",
            "Basic Python syntax (`exercises/01–03`).",
            "`02-oop-intermediate-house-rules.ipynb`",
            "recipe cards, alarm clocks, shopping carts",
            [
                "Explain **class vs instance** using everyday metaphors.",
                "Initialize objects with `__init__` and store **state** on `self`.",
                "Call **methods** that change or read that state.",
            ],
            [
                "Recipe blueprint vs one tray of cookies",
                "`AlarmClock` — ringing behavior",
                "`CoffeeMaker` — simple actions",
                "Exercise — contacts list like your phone",
            ],
        )
    )

    cells.append(
        cell_md(
            """## 1 · Class = blueprint, instance = one real thing

**Daily life:** Architectural drawings describe *every* house on a street, but **your** house is one physical building with its own paint color.

**In Python:** `class CookieTray:` describes trays in general; `tray_a = CookieTray()` is **one** tray with its own cookie count."""
        )
    )
    cells.append(
        cell_code(
            '''class CookieTray:
    """Blueprint for trays leaving the oven."""

    def __init__(self, flavor: str, count: int) -> None:
        self.flavor = flavor
        self.count = count

    def eat_one(self) -> None:
        if self.count > 0:
            self.count -= 1

    def describe(self) -> str:
        return f"{self.count}× {self.flavor} cookies"


birthday = CookieTray("chocolate", 12)
birthday.eat_one()
print(birthday.describe())'''
        )
    )

    cells.append(
        cell_md(
            """## 2 · `AlarmClock` — attributes + behavior together

**Daily life:** Two bedside alarms can show **different times** but **both know how to snooze**.

**Programming idea:** Data (`hour`, `minute`) lives next to actions (`snooze`)."""
        )
    )
    cells.append(
        cell_code(
            '''class AlarmClock:
    def __init__(self, label: str, hour: int = 7, minute: int = 0) -> None:
        self.label = label
        self.hour = hour
        self.minute = minute

    def display(self) -> str:
        return f"[{self.label}] {self.hour:02d}:{self.minute:02d}"

    def snooze(self, minutes: int = 9) -> None:
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1


work = AlarmClock("Weekdays", 6, 55)
work.snooze()
print(work.display())'''
        )
    )

    cells.append(
        cell_md(
            """## 3 · `CoffeeMaker` — methods encode habits

**Daily life:** Push-button steps (`grind`, `brew`) reuse the same machine state (`beans_left`)."""
        )
    )
    cells.append(
        cell_code(
            '''class CoffeeMaker:
    def __init__(self, beans_grams: float) -> None:
        self.beans_grams = beans_grams

    def grind(self, grams: float) -> None:
        self.beans_grams = max(0.0, self.beans_grams - grams)

    def can_brew(self, shot_grams: float = 18.0) -> bool:
        return self.beans_grams >= shot_grams


kitchen = CoffeeMaker(40)
kitchen.grind(10)
print("Enough for espresso?", kitchen.can_brew())'''
        )
    )

    cells.append(
        cell_md(
            """### Exercise — Phone contacts (beginner)

**Daily life:** Your contacts app stores names → numbers and lets you search.

Implement `ContactBook`:

- `add(name, phone)` — store contact (`phone` string ok).
- `find(prefix)` — return **sorted list** of names that **start with** `prefix` (case-sensitive is fine).

Starter asserts included."""
        )
    )
    cells.append(
        cell_code(
            '''class ContactBook:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, name: str, phone: str) -> None:
        raise NotImplementedError

    def find(self, prefix: str) -> list[str]:
        raise NotImplementedError


cb = ContactBook()
cb.add("Sam", "555-0101")
cb.add("Sara", "555-0102")
cb.add("Mo", "555-0199")
assert set(cb.find("Sa")) == {"Sam", "Sara"}
print("Exercise OK")'''
        )
    )
    cells.append(
        solution_md(
            "ContactBook",
            "class ContactBook:\n    def __init__(self) -> None:\n        self._contacts: dict[str, str] = {}\n\n    def add(self, name: str, phone: str) -> None:\n        self._contacts[name] = phone\n\n    def find(self, prefix: str) -> list[str]:\n        hits = [n for n in self._contacts if n.startswith(prefix)]\n        return sorted(hits)",
        )
    )

    write_nb("01-oop-beginner-blueprints-and-objects.ipynb", cells)


def nb_intermediate() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "OOP-2",
            "House rules — hiding details, families & backpacks",
            "Intermediate",
            "`01-oop-beginner-blueprints-and-objects.ipynb`",
            "`03-oop-advanced-contracts-and-plugins.ipynb`",
            "piggy banks, bikes vs cars, backpacks packing lists",
            [
                "Use **encapsulation** (leading `_`) like a PIN panel hiding balance digits.",
                "Tell **inheritance** (`Vehicle`) from **composition** (`Backpack` holds pens).",
                "Optional `@property` for validation — thermostat can't read −400°F.",
            ],
            [
                "Encapsulation — piggy bank",
                "`@property` thermostat bounds",
                "Inheritance — vehicles",
                "Composition — backpack",
                "Exercise — gym membership tiers",
            ],
        )
    )

    cells.append(
        cell_md(
            """## 1 · Encapsulation — piggy bank hides counting coins

**Daily life:** Kids shake a sealed piggy bank—they hear coins but can't silently steal without **breaking rules**. Methods (`deposit`, `safe_balance_hint`) are the **official doors**.

Python convention: `_balance` signals \"please don't touch directly\"; technically possible, but rude like popping open someone's bank."""
        )
    )
    cells.append(
        cell_code(
            '''class PiggyBank:
    def __init__(self) -> None:
        self._cents = 0

    def deposit(self, dollars: float) -> None:
        if dollars < 0:
            raise ValueError("no stealing via negative deposits")
        self._cents += int(round(dollars * 100))

    def shake_estimate(self) -> str:
        if self._cents == 0:
            return "empty"
        if self._cents < 500:
            return "light"
        return "heavy"


pig = PiggyBank()
pig.deposit(3.40)
pig.deposit(2)
print(pig.shake_estimate())'''
        )
    )

    cells.append(
        cell_md(
            """## 2 · `@property` — thermostat clamp

**Daily life:** Wall thermostat displays °F but refuses absurd targets—same idea as getters/setters with validation."""
        )
    )
    cells.append(
        cell_code(
            '''class Thermostat:
    def __init__(self) -> None:
        self._temp_f = 68.0

    @property
    def temp_f(self) -> float:
        return self._temp_f

    @temp_f.setter
    def temp_f(self, value: float) -> None:
        if not (55 <= value <= 85):
            raise ValueError("unrealistic comfort zone")
        self._temp_f = value


t = Thermostat()
t.temp_f = 72
print(t.temp_f)'''
        )
    )

    cells.append(
        cell_md(
            """## 3 · Inheritance — bicycles & cars share \"start journey\"

**Daily life:** Different vehicles **share** ideas (they move people) but implement movement differently."""
        )
    )
    cells.append(
        cell_code(
            '''class Vehicle:
    def __init__(self, brand: str) -> None:
        self.brand = brand

    def commute_noise(self) -> str:
        raise NotImplementedError("each vehicle sounds different")


class Bicycle(Vehicle):
    def commute_noise(self) -> str:
        return "tick tick tick"


class Bus(Vehicle):
    def commute_noise(self) -> str:
        return "whoosh-air-brakes"


for v in (Bicycle("Trek"), Bus("CityLine")):
    print(v.brand, "→", v.commute_noise())'''
        )
    )

    cells.append(
        cell_md(
            """## 4 · Composition — backpack *has* supplies

**Daily life:** Backpack isn't a \"kind of pen\"; it **contains** pens—**has-a**, not **is-a**.

This mirrors AI stacks: `Pipeline` **has** `Retriever` + `LLMClient`.""")
    )
    cells.append(
        cell_code(
            '''class Pen:
    def __init__(self, ink_color: str) -> None:
        self.ink_color = ink_color


class Backpack:
    def __init__(self) -> None:
        self.items: list[Pen] = []

    def pack(self, pen: Pen) -> None:
        self.items.append(pen)

    def palette(self) -> list[str]:
        return [p.ink_color for p in self.items]


bag = Backpack()
bag.pack(Pen("blue"))
bag.pack(Pen("black"))
print(bag.palette())'''
        )
    )

    cells.append(
        cell_md(
            """### Exercise — gym membership tiers

**Daily life:** Basic vs Premium members **share** check-in but Premium unlocks sauna visits.

Requirements:

1. Base class `Member(name)` with method `benefits() -> list[str]` returning base perks (e.g. `["locker"]`).
2. `PremiumMember` adds `"sauna"` **without breaking** basic perks.
3. `describe(member)` prints `"Name — perk1, perk2"` sorted alphabetically."""
        )
    )
    cells.append(
        cell_code(
            '''class Member:
    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def benefits(self) -> list[str]:
        raise NotImplementedError


class PremiumMember(Member):
    def benefits(self) -> list[str]:
        raise NotImplementedError


def describe(member: Member) -> str:
    raise NotImplementedError


m = Member("Alex")
p = PremiumMember("Jordan")
assert "locker" in m.benefits()
assert "sauna" in p.benefits() and "locker" in p.benefits()
assert describe(p).startswith("Jordan —")
print("Exercise OK")'''
        )
    )
    cells.append(
        solution_md(
            "gym tiers",
            '''class Member:
    def __init__(self, name: str) -> None:
        self.name = name

    def benefits(self) -> list[str]:
        return ["locker"]


class PremiumMember(Member):
    def benefits(self) -> list[str]:
        return sorted(super().benefits() + ["sauna"])


def describe(member: Member) -> str:
    perks = ", ".join(sorted(member.benefits()))
    return f"{member.name} — {perks}"''',
        )
    )

    write_nb("02-oop-intermediate-house-rules.ipynb", cells)


def nb_advanced() -> None:
    cells: list[dict[str, Any]] = []
    cells.extend(
        banner(
            "OOP-3",
            "Contracts & plugins — payments, chargers, smart-home hubs",
            "Advanced",
            "`02-oop-intermediate-house-rules.ipynb`",
            "`exercises/08-advanced-typing-protocols-dataclasses.ipynb`",
            "cash vs tap-to-pay, USB charging bars, Alexa-style plugins",
            [
                "Use `@dataclass(frozen=True)` for immutable IDs.",
                "Combine **ABC** + subclasses like interchangeable checkout lanes.",
                "Use **`typing.Protocol`** for \"anything that charges phones\".",
                "Recognize dunder hooks (`__repr__`) as readable receipts.",
            ],
            [
                "Frozen dataclass — library card",
                "ABC checkout lanes",
                "Protocol charging kiosk",
                "`__repr__` receipts",
                "Exercise — smart-home toggle hub",
            ],
        )
    )

    cells.append(
        cell_md(
            """## 1 · Frozen dataclass — library card barcode

**Daily life:** Plastic library card **number shouldn't mutate** after issuance—perfect match for `frozen=True`.""")
    )
    cells.append(
        cell_code(
            '''from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class LibraryCard:
    holder: str
    barcode: str


card = LibraryCard("Taylor", "5901234567890")
print(card)
try:
    card.barcode = "nope"
except Exception as e:
    print(type(e).__name__)'''
        )
    )

    cells.append(
        cell_md(
            """## 2 · ABC — checkout accepts cash or tap-to-pay

**Daily life:** Cashier cares that payment **settles**, not whether bills or NFC chip—**abstract interface**, concrete behaviors.""")
    )
    cells.append(
        cell_code(
            '''from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def settle(self, amount_cents: int) -> str:
        ...


class CashPayment(PaymentMethod):
    def settle(self, amount_cents: int) -> str:
        return f"counted ${amount_cents/100:.2f} cash"


class TapPayment(PaymentMethod):
    def settle(self, amount_cents: int) -> str:
        return f"tapped NFC ${amount_cents/100:.2f}"


def checkout(method: PaymentMethod, cents: int) -> None:
    print(method.settle(cents))

checkout(CashPayment(), 425)
checkout(TapPayment(), 425)'''
        )
    )

    cells.append(
        cell_md(
            """## 3 · Protocol — charging kiosk accepts mystery gadgets

**Daily life:** Airport kiosk doesn't ask \"what brand phone?\" — only checks \"does **Chargeable** plug work?\" (`Protocol`).""")
    )
    cells.append(
        cell_code(
            '''from typing import Protocol, runtime_checkable

@runtime_checkable
class Chargeable(Protocol):
    def charge_minutes(self, minutes: int) -> int:
        ...


class Phone:
    def charge_minutes(self, minutes: int) -> int:
        return minutes * 2  # fake percent gain


class Laptop:
    def charge_minutes(self, minutes: int) -> int:
        return minutes


def kiosk_boost(device: Chargeable, minutes: int) -> None:
    gain = device.charge_minutes(minutes)
    print(f"kiosk delivered ~{gain}% juice")


kiosk_boost(Phone(), 15)
print(isinstance(Laptop(), Chargeable))'''
        )
    )

    cells.append(
        cell_md(
            """## 4 · `__repr__` — readable grocery receipts

**Daily life:** Receipt lines formatted uniformly — Python uses `__repr__` / dataclass defaults for debugging.""")
    )
    cells.append(
        cell_code(
            '''from dataclasses import dataclass

@dataclass
class CartLine:
    sku: str
    qty: int
    unit_usd: float

    def total(self) -> float:
        return self.qty * self.unit_usd


print([CartLine("milk", 2, 3.5), CartLine("bread", 1, 4.25)])'''
        )
    )

    cells.append(
        cell_md(
            """### Exercise — smart-home hub (`Protocol`)

**Daily life:** Wall tablet toggles lamps **without knowing vendor firmware** — protocol talks \"toggle\" only.

Requirements:

1. Define `@runtime_checkable` protocol `ToggleDevice` with `label() -> str` and `toggle() -> None`.
2. Classes `DeskLamp` and `Fan` implement it (track `_on` bool).
3. `SmartHub.toggle_all(devices)` prints each label then toggles."""
        )
    )
    cells.append(
        cell_code(
            '''from typing import Protocol, runtime_checkable

@runtime_checkable
class ToggleDevice(Protocol):
    def label(self) -> str: ...
    def toggle(self) -> None: ...

class DeskLamp:
    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def label(self) -> str:
        raise NotImplementedError

    def toggle(self) -> None:
        raise NotImplementedError


class Fan:
    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def label(self) -> str:
        raise NotImplementedError

    def toggle(self) -> None:
        raise NotImplementedError


class SmartHub:
    def toggle_all(self, devices: list[ToggleDevice]) -> None:
        raise NotImplementedError


# After implementing, uncomment:
# hub = SmartHub()
# hub.toggle_all([DeskLamp("Reading"), Fan("Ceiling")])
print("Implement classes, then uncomment the demo.")'''
        )
    )
    cells.append(
        solution_md(
            "smart-home hub",
            '''from typing import Protocol, runtime_checkable

@runtime_checkable
class ToggleDevice(Protocol):
    def label(self) -> str: ...
    def toggle(self) -> None: ...

class DeskLamp:
    def __init__(self, name: str) -> None:
        self._name = name
        self._on = False

    def label(self) -> str:
        return f"Lamp:{self._name}"

    def toggle(self) -> None:
        self._on = not self._on


class Fan:
    def __init__(self, name: str) -> None:
        self._name = name
        self._on = False

    def label(self) -> str:
        return f"Fan:{self._name}"

    def toggle(self) -> None:
        self._on = not self._on


class SmartHub:
    def toggle_all(self, devices: list[ToggleDevice]) -> None:
        for d in devices:
            print(d.label())
            d.toggle()''',
        )
    )

    write_nb("03-oop-advanced-contracts-and-plugins.ipynb", cells)


def main() -> None:
    nb_beginner()
    nb_intermediate()
    nb_advanced()
    print("Done ->", OUT_DIR)


if __name__ == "__main__":
    main()
