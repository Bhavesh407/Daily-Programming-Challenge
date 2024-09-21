def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]  
            if not prefix:
                return "" 
    
    return prefix

def main():
    user_input = input("")
    strs = [s.strip() for s in user_input.split(",")]
    result = longest_common_prefix(strs)

    if result:
        print(result)
    else:
        print("There is no common prefix among the provided strings.")

if __name__ == "__main__":
    main()
