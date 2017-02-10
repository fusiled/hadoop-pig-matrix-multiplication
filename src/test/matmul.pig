SET default_parallel n;
matrix1 = LOAD 'mat1' AS (row,col,value);
matrix2 = LOAD 'mat1' AS (row,col,value);
A = JOIN matrix1 BY col FULL OUTER, matrix2 BY row;
B = FOREACH A GENERATE matrix1::row AS m1r, matrix2::col AS m2c, (matrix1::value)*(matrix2::value) AS value;
C = GROUP B BY (m1r, m2c);
multiplied_matrices = FOREACH C GENERATE group.$0 as row, group.$1 as col, SUM(B.value) AS val;
store multiplied_matrices into 'matmul_out'; 