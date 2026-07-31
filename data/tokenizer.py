from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        corpus_split = list(corpus)
        
        merges = []
        for _ in range(num_merges):
            if len(corpus_split) < 2:
                break

            pairs = {} # count each adjacent pair frequencies
            for i in range(len(corpus_split) - 1):
                pair = (corpus_split[i], corpus_split[i + 1]) # for each pair
                pairs[pair] = pairs.get(pair, 0) + 1
            
            if not pairs:
                break
            
            # find the most frequent pair:
            best_count = max(pairs.values())
            candidates = sorted(p for p, c in pairs.items() if c == best_count)
            best = candidates[0]

            merges.append([best[0], best[1]])

            # merge all the non-overlapping pairs left to right
            new_corpus_split = []
            i = 0
            while i < len(corpus_split):
                if i < len(corpus_split) - 1 and corpus_split[i] == best[0] and corpus_split[i + 1] == best[1]:
                    new_corpus_split.append(best[0] + best[1])
                    i += 2
                else:
                    new_corpus_split.append(corpus_split[i])
                    i += 1
            corpus_split = new_corpus_split

        return merges

        

        
