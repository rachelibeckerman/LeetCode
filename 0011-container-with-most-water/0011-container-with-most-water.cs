public class Solution {
    public int MaxArea(int[] height) {

        int max = 0;
        int i = 0 , j = height.Length - 1;

        while(i < j){
            max = Math.Max( Math.Min(height[i],height[j]) * (j - i) ,max);
            if(height[i] == height[j]){
                i++;
                j--;
            }
            else if(height[i] < height[j])
                i++;
            else
                j--;
        }
        return max;
    }
}