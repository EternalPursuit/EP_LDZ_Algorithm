matrix_origin_encoded = [int(item_element) for item_element in input().split()]
matrix_m_rows = matrix_origin_encoded[0]
matrix_n_cols = matrix_origin_encoded[1]
matrix_encoded_slices = matrix_origin_encoded[2:]
new_matrix_ori = [[0]*matrix_n_cols for _ in range(matrix_m_rows)]
row_cur = 0
col_cur = 0
for i in range(0, len(matrix_encoded_slices), 2):
    val_nums = matrix_encoded_slices[i+1]
    values = matrix_encoded_slices[i]
    # 依据当前的位置计算将要到达的位置
    index_count = 0
    while col_cur < matrix_n_cols and row_cur <matrix_m_rows and index_count < val_nums:
        new_matrix_ori[row_cur][col_cur] = values
        if col_cur < matrix_n_cols:
            col_cur += 1
            index_count += 1
        if col_cur == matrix_n_cols:
            col_cur = 0
            row_cur += 1
print()
for i in range(matrix_m_rows):
    print(*new_matrix_ori[i])
target_row,target_col = map(int,input().split())
print(new_matrix_ori[target_row][target_col])