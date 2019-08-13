
class Solution:
    def lengthOfLongestSubstring(self, src: str) -> int:
        """
        採用 Sliding Window 的策略，來累積與計算最長不重複字串
        """
        record_map = []
        longest = left = curr = 0
        substr = ""
        while(curr < len(src)):
            # 不是起始字元，且是否目前的字元有在和目前最長的子字串有字元重複
            if curr > 0 and (src[curr] in substr):
                # 有的話來找出索引，在左邊 Slide 位置不超過目前現在索引前一位為前提下
                # 若由左向右 slide window 沒有發現重複，則一直移動直到最後
                while((len(substr) > left) and substr[left] != src[curr]):
                    left += 1
                # 先加入新的字元進去 (如此向右移動才有空間)
                substr += src[curr]
                # 把重複字元以前的子字串捨棄
                substr = substr[left + 1:]
                left = 0
            else:
                # 加入目前的字元到字串中
                substr += src[curr]
            # 紀錄此次的字段作為長度統計
            record_map.append(substr)
            # 計算目前最長長度
            longest = len(substr) if len(substr) > longest else longest
            curr += 1
        # print(record_map)
        return longest
