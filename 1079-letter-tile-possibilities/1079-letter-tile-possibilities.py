class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        used = [False]*len(tiles)
        def generate_sequence(tiles, current, used, sequences):

            sequences.add(current)
            for pos, char in enumerate(tiles):
                if not used[pos]:
                    used[pos] = True
                    generate_sequence(tiles, current + char, used, sequences)
                    used[pos] = False

        generate_sequence(tiles, "", used, sequences)

        return len(sequences) - 1
