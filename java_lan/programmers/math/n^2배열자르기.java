class Solution {
    public int[] solution(int n, long left, long right) {
        int len = (int) (right - left) + 1;
        int[] answer = new int[len];
        int index = 0;
        
        for(long i = left; i <= right; i++) {
            answer[index++] = (int) Math.max(i / n, i % n) + 1;
        }
        
        return answer;
    }
}