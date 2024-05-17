class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {

        if(matrix.empty())  return;
        


        size_t n = matrix.size();
        size_t m = matrix[0].size();
        bool first_row_has_zero = false;
        bool first_col_has_zero = false;

        // Check first row and column: handle separately at the end 
        for(size_t j=0; j<m; j++) {
            if(matrix[0][j] == 0) {
                first_row_has_zero = true;
                break;
            }    
        }

        for(size_t i=0; i<n; i++) {
            if(matrix[i][0] == 0)
                first_col_has_zero = true;
                break;    
        }


        // Use the first row and column to mark zeros 
        for(size_t i=1; i<n; ++i) {
            for(size_t j=1; j<m; ++j) {
                if(matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }        
        }

        // Zero out the marked rows and columns 
        for(size_t i=1; i<n; ++i) {
            for(size_t j=1; j<m; ++j) {
                if( matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }        
        }

        // Zero out first row if needed
        if(first_row_has_zero) {
            for(size_t j=0; j<m; ++j)
                matrix[0][j] = 0;
        }

        // Zero out first col if needed
        if(first_col_has_zero) {
            for(size_t i=0; i<n; ++i)
                matrix[i][0] = 0;
        }
    }
};