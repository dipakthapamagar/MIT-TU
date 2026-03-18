set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))
union = set1 | set2
intersection = set1 & set2
difference1 = set1 - set2
difference2 = set2 - set1
symmetric_difference = set1 ^ set2
print("\nSet 1:", set1)
print("Set 2:", set2)
print("\nUnion:", union)
print("Intersection:", intersection)
print("Difference (Set1 - Set2):", difference1)
print("Difference (Set2 - Set1):", difference2)
print("Symmetric Difference:", symmetric_difference)