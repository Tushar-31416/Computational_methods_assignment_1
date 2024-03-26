#include <stdio.h>
#include <gsl/gsl_linalg.h>

int main() {
    const int N = 5;

    double A[N][N] = {
        {4.0, 1.0, 1.0, 0.0, 1.0},
        {-1.0, -3.0, 1.0, 1.0, 0.0},
        {2.0, 1.0, 5.0, -1.0, -1.0},
        {-1.0, -1.0, -1.0, 4.0, 0.0},
        {0.0, 2.0, -1.0, 1.0, 4.0}
    };

    gsl_matrix_view m = gsl_matrix_view_array(&A[0][0], N, N);

    gsl_permutation *p = gsl_permutation_alloc(N);
    int sig;
    gsl_linalg_LU_decomp(&m.matrix, p, &sig);
    gsl_matrix *L = gsl_matrix_alloc(N, N);
    gsl_matrix *U = gsl_matrix_alloc(N, N);
    gsl_matrix_memcpy(L, &m.matrix);
    gsl_matrix_memcpy(U, &m.matrix);
    gsl_linalg_LU_decomp(&m.matrix, p, &sig);
    gsl_matrix_set_identity(L);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i < j) {
                gsl_matrix_set(L, i, j, gsl_matrix_get(&m.matrix, i, j));
            } else if (i == j) {
                gsl_matrix_set(L, i, j, 1.0); 
            } else {
                gsl_matrix_set(U, i, j, 0.0); 
            }
        }
    }

  
    printf("Original Matrix:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%8.3f ", A[i][j]);
        }
        printf("\n");
    }

    printf("\nAfter decomposition (L*U):\n");
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, L, U, 0.0, &m.matrix);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%8.3f ", gsl_matrix_get(&m.matrix, i, j));
        }
        printf("\n");
    }

    gsl_permutation_free(p);
    gsl_matrix_free(L);
    gsl_matrix_free(U);

    return 0;
}
