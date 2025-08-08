heights = [2, 1, 5, 6, 2, 3]
max_area = 0

for i in range(len(heights)):
    height = heights[i]
    
    # Expand left
    left = i
    while left > 0 and heights[left - 1] >= height:
        left -= 1

    # Expand right
    right = i
    while right < len(heights) - 1 and heights[right + 1] >= height:
        right += 1

    width = right - left + 1
    max_area = max(max_area, height * width)

print(max_area)
