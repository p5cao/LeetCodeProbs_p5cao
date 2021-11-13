class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        // convert string to char array
        char[] arrS = s.toCharArray();
        char[] arrP = p.toCharArray();
        
        // create result array
        List<Integer> ans = new ArrayList<>();
        // 2 int arrays to store the element needed and element traversed by the window
        int[] needs = new int[26];
        int[] window = new int[26];
        
        // store elements in arrP to needs array
        
        for (int i = 0; i < arrP.length; i++){
            needs[arrP[i] - 'a'] += 1;
       }
        
        // left right pointer of the sliding window
        int left = 0;
        int right = 0;
        
        while (right < arrS.length) {
            int curR = arrS[right] -'a';
            //store number of elements in window
            right++;
            window[curR] += 1;
            
            while (window[curR] > needs[curR]){
                int curL = arrS[left] - 'a';
                left ++;
                // reduce number of the elements visted by left pointer by 1
                window[curL] -= 1;
            }
            // add all the left pointer element to ans List
            if (right - left == arrP.length){
                ans.add(left);
            }
        }
        return ans;
    }
    
}