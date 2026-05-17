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
                "**Progressive drills** — water bottle → laundry → parking meter",
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
            """---

## Progressive examples — **easy → harder**

Standalone cells below ramp difficulty: **one number + one verb** → **small collections** → **rules + guards**. Compare each class's **state** (`self....`) before and after methods run."""
        )
    )

    cells.append(
        cell_md(
            """### A · Easiest — **water bottle** (one dial: milliliters left)

**Daily life:** Each sip drains liquid; you can't magically sip below zero."""
        )
    )
    cells.append(
        cell_code(
            '''class WaterBottle:
    def __init__(self, milliliters: float) -> None:
        self.ml = milliliters

    def sip(self, amount: float) -> float:
        """Return how much was actually swallowed."""
        swallowed = min(amount, self.ml)
        self.ml -= swallowed
        return swallowed


bottle = WaterBottle(500)
print("sip", bottle.sip(120), "left", bottle.ml)
print("sip huge", bottle.sip(9999), "left", bottle.ml)'''
        )
    )

    cells.append(
        cell_md(
            """### B · Easy — **laundry basket** (hidden list)

**Daily life:** Toss socks in, grab something to wash—internal pile grows/shrinks without exposing raw chaos."""
        )
    )
    cells.append(
        cell_code(
            '''class LaundryBasket:
    def __init__(self) -> None:
        self._pile: list[str] = []

    def toss(self, garment: str) -> None:
        self._pile.append(garment)

    def grab_any(self) -> str | None:
        return self._pile.pop() if self._pile else None

    def load_size(self) -> int:
        return len(self._pile)


hamper = LaundryBasket()
hamper.toss("sock")
hamper.toss("tee")
print("size", hamper.load_size(), "grabbed", hamper.grab_any(), "remaining", hamper.load_size())'''
        )
    )

    cells.append(
        cell_md(
            """### C · Medium — **parking meter** (accumulate then burn time)

**Daily life:** Coins buy minutes; driving away consumes minutes until expired."""
        )
    )
    cells.append(
        cell_code(
            '''class ParkingMeter:
    def __init__(self) -> None:
        self.minutes_left = 0

    def add_quarters(self, quarters: int) -> None:
        if quarters < 0:
            raise ValueError("no negative quarters")
        self.minutes_left += quarters * 15  # toy rule: 15 min each

    def drive_minutes(self, minutes: int) -> None:
        self.minutes_left = max(0, self.minutes_left - minutes)

    def is_expired(self) -> bool:
        return self.minutes_left == 0


m = ParkingMeter()
m.add_quarters(2)
print("after coins", m.minutes_left)
m.drive_minutes(40)
print("after commute", m.minutes_left, "expired?", m.is_expired())'''
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
                "**Progressive drills** — mailbox → fuel tank → coach roster",
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
    print(v.brand, "->", v.commute_noise())'''
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
            """---

## Progressive examples — **easy → harder**

Same ideas as above—now layer **privacy**, **validated fuel**, **teams built from people**."""
        )
    )

    cells.append(
        cell_md(
            """### A · Easy — **mailbox** (letters hidden inside)

**Daily life:** Slot accepts envelopes; nosy neighbors only see **how full**, not love-letter contents."""
        )
    )
    cells.append(
        cell_code(
            '''class Mailbox:
    def __init__(self) -> None:
        self._letters: list[str] = []

    def deposit(self, note: str) -> None:
        if not note.strip():
            raise ValueError("empty mail")
        self._letters.append(note.strip())

    def count(self) -> int:
        return len(self._letters)


box = Mailbox()
box.deposit("dentist reminder")
box.deposit("postcard")
print("waiting letters:", box.count())'''
        )
    )

    cells.append(
        cell_md(
            """### B · Medium — **fuel tank** (`@property` + clamp)

**Daily life:** Gauge can't display negative gallons or overflow the tank."""
        )
    )
    cells.append(
        cell_code(
            '''class FuelTank:
    def __init__(self, max_gallons: float, initial: float) -> None:
        self._cap = max_gallons
        if not (0 <= initial <= max_gallons):
            raise ValueError("bad fill level")
        self._gallons = initial

    @property
    def gallons(self) -> float:
        return self._gallons

    @gallons.setter
    def gallons(self, value: float) -> None:
        if not (0 <= value <= self._cap):
            raise ValueError("fuel must fit tank")
        self._gallons = value


tank = FuelTank(max_gallons=15, initial=10)
tank.gallons = tank.gallons - 3  # explicit read/set avoids augmented-assign quirks on properties
print("after highway stretch", tank.gallons)
tank.gallons = 14
print("filled to", tank.gallons)'''
        )
    )

    cells.append(
        cell_md(
            """### C · Harder — **coach roster** (composition over inheritance)

**Daily life:** Coach **has** athletes on a clipboard—coach isn't \"a type of athlete\"; it's a role managing many."""
        )
    )
    cells.append(
        cell_code(
            '''class Athlete:
    def __init__(self, name: str, sport: str) -> None:
        self.name = name
        self.sport = sport


class Coach:
    def __init__(self, name: str) -> None:
        self.name = name
        self._roster: list[Athlete] = []

    def sign(self, athlete: Athlete) -> None:
        self._roster.append(athlete)

    def roster_summary(self) -> str:
        parts = [f"{a.name} ({a.sport})" for a in self._roster]
        return ", ".join(sorted(parts))


c = Coach("Rivera")
c.sign(Athlete("Bo", "soccer"))
c.sign(Athlete("Ali", "track"))
print(c.roster_summary())'''
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
                "**Progressive drills** — delivery states → ticket equality → cart merge → addon registry",
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
            """---

## Progressive examples — **easy → hardest**

Shippable AI services reuse these tricks: **finite state**, **value identity**, **merging snapshots**, **plugin menus**."""
        )
    )

    cells.append(
        cell_md(
            """### A · Easy — **delivery order** (tiny state machine)

**Daily life:** Warehouse won't ship before packing—illegal jumps raise loudly (bugs surface early)."""
        )
    )
    cells.append(
        cell_code(
            '''class DeliveryOrder:
    def __init__(self, oid: str) -> None:
        self.oid = oid
        self.status = "placed"

    def pack(self) -> None:
        if self.status != "placed":
            raise ValueError(f"cannot pack while status={self.status}")
        self.status = "packed"

    def ship(self) -> None:
        if self.status != "packed":
            raise ValueError(f"cannot ship while status={self.status}")
        self.status = "shipped"


order = DeliveryOrder("AI-409")
order.pack()
print(order.oid, order.status)
try:
    order.pack()
except ValueError as err:
    print("blocked:", err)'''
        )
    )

    cells.append(
        cell_md(
            """### B · Medium — **seat tickets** (`frozen` dataclass equality)

**Daily life:** Two barcode scans reference the **same seat** even though they're different slips—`frozen` dataclass compares **values**, not memory ids."""
        )
    )
    cells.append(
        cell_code(
            '''from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class SeatTicket:
    row: str
    seat: int


scan_a = SeatTicket("M", 7)
scan_b = SeatTicket("M", 7)
print("equal?", scan_a == scan_b, "same object?", scan_a is scan_b)'''
        )
    )

    cells.append(
        cell_md(
            """### C · Medium-hard — **merging grocery carts** (`__add__`)

**Daily life:** Roommate grabs apples, you grab oat milk—checkout merges quantities **without destroying** original carts."""
        )
    )
    cells.append(
        cell_code(
            '''class GroceryCart:
    def __init__(self) -> None:
        self.items: dict[str, int] = {}

    def add(self, sku: str, qty: int = 1) -> None:
        self.items[sku] = self.items.get(sku, 0) + qty

    def __add__(self, other: GroceryCart) -> GroceryCart:
        merged = GroceryCart()
        for sku, qty in self.items.items():
            merged.add(sku, qty)
        for sku, qty in other.items.items():
            merged.add(sku, qty)
        return merged

    def __repr__(self) -> str:
        return f"GroceryCart({self.items})"


mine = GroceryCart()
mine.add("apple", 3)
roommate = GroceryCart()
roommate.add("apple", 1)
roommate.add("oat milk", 2)
print(mine + roommate)'''
        )
    )

    cells.append(
        cell_md(
            """### D · Hardest — **coffee addon registry** (plugin-style pricing)

**Daily life:** Cafeteria registers syrups/shots once; pricing algorithm sums unknown extras safely."""
        )
    )
    cells.append(
        cell_code(
            '''class DrinkMenu:
    def __init__(self) -> None:
        self._addons: dict[str, float] = {}

    def register_addon(self, name: str, price_usd: float) -> None:
        self._addons[name] = price_usd

    def latte_price(self, base_usd: float = 4.5, extras: list[str] | None = None) -> float:
        extras = extras or []
        total = base_usd
        for label in extras:
            total += self._addons.get(label, 0.0)
        return round(total, 2)


menu = DrinkMenu()
menu.register_addon("oat milk", 0.8)
menu.register_addon("extra shot", 1.2)
print(menu.latte_price(extras=["oat milk", "extra shot"]))'''
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
