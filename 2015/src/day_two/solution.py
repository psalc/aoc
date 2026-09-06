import curate

def surface_area(l, w, h) -> int:
    return 2*l*w + 2*w*h + 2*h*l

def smallest_side(l, w, h) -> int:
    return min(l*w, w*h, l*h)

def required_paper(l, w, h) -> int:
    return surface_area(l, w, h) + smallest_side(l, w, h)

def smallest_perimeter(l, w, h) -> int:
    return min(2*l + 2*w, 2*w + 2*h, 2*l + 2*h)

def bow_length(l, w, h) -> int:
    return l*w*h

def required_ribbon(l, w, h) -> int:
    return smallest_perimeter(l, w, h) + bow_length(l, w, h)

def main():
    input = curate.read_input(2)
    lines = input.splitlines()
    dimensions = [tuple(map(int, line.split('x'))) for line in lines]
    print(f"Total square feet of wrapping paper required: {sum([required_paper(*d) for d in dimensions])}")
    print(f"Total feet of ribbon: {sum([required_ribbon(*d) for d in dimensions])}")
    
if __name__ == "__main__":
    main()