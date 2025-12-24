def calc_avg(numbers: list[float]) -> float:
    if not numbers:
        return 0.0  
    return sum(numbers) / len(numbers)
def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    fio = " ".join(parts)
    if capitalize:
        return fio.title()        
    return fio
def filter_scores(data_dict: dict[str, int], min_value: int) -> dict[str, int]:
    result = {}
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value            
    return result
if __name__ == "__main__":
    print("calc_avg([10, 20, 30, 40]):", calc_avg([10, 20, 30, 40]))
    print("calc_avg([]):", calc_avg([]))
    print('\nfmt_fio(["петров", "иван", "сергеевич"]):', 
          fmt_fio(["петров", "иван", "сергеевич"]))
    print('fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False):',
          fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False))
    scores = {"math": 95, "history": 78, "english": 88, "art": 92}
    print("\nfilter_scores(scores, 90):", filter_scores(scores, 90))