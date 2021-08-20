def count_matching_nums(seq1, seq2):
    return len(set(seq1) & set(seq2))


print(count_matching_nums([4, 3, 5, 1, 2], [1, 2]))  # 2
