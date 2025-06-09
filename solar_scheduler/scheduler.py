from typing import Dict, List, Tuple
from .models import Building, Employee
from .rules import requirements

def _pick(pool, filt, amount):
    chosen = [e for e in pool if filt(e)][:amount]
    if len(chosen) < amount:
        return None
    for c in chosen:
        pool.remove(c)
    return chosen

def schedule(
    buildings: List[Building],
    employees: List[Employee],
) -> Dict[int, List[Tuple[Building, List[Employee]]]]:
    day_pool = {d: [e for e in employees if e.available_days[d]] for d in range(5)}
    plan = {d: [] for d in range(5)}
    for b in buildings:
        for day in range(5):
            scratch = day_pool[day].copy()
            crew: List[Employee] = []
            for filt, amount in requirements(b):
                picked = _pick(scratch, filt, amount)
                if picked is None:
                    break
                crew.extend(picked)
            else:
                # commit
                for e in crew:
                    day_pool[day].remove(e)
                plan[day].append((b, crew))
                break
    return plan
