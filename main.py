import argparse
import colorsys

def hex_to_rgb(h):
    h = h.strip().lstrip('#')
    if len(h) != 6:
        raise ValueError('HEX must be 6 chars')
    return tuple(int(h[i:i+2], 16) for i in (0,2,4))

def rgb_to_hex(rgb):
    return '#%02X%02X%02X' % rgb

def rotate_hue(rgb, degrees):
    r,g,b = [x/255 for x in rgb]
    h,l,s = colorsys.rgb_to_hls(r,g,b)
    h = (h + degrees/360.0) % 1.0
    rr,gg,bb = colorsys.hls_to_rgb(h,l,s)
    return (round(rr*255), round(gg*255), round(bb*255))

def palette(base_hex):
    base = hex_to_rgb(base_hex)
    return {
        'base': rgb_to_hex(base),
        'complementary': rgb_to_hex(rotate_hue(base, 180)),
        'analogous_1': rgb_to_hex(rotate_hue(base, -30)),
        'analogous_2': rgb_to_hex(rotate_hue(base, 30)),
        'triadic_1': rgb_to_hex(rotate_hue(base, 120)),
        'triadic_2': rgb_to_hex(rotate_hue(base, 240)),
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--base', required=True, help='Base HEX color, e.g. #5B8CFF')
    args = p.parse_args()

    pal = palette(args.base)
    print('Generated palette')
    for k,v in pal.items():
        print(f'- {k}: {v}')

if __name__ == '__main__':
    main()
