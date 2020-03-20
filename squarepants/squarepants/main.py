#! python3
import cv2
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image",
        help="Path to image file"
    )
    args = parser.parse_args()
    img = cv2.imread(args.image, cv2.IMREAD_COLOR)

    h, w, _ = img.shape
    pad, sample_p, blur = 40, 90, 70
    sq_hw = max(h, w) + 2*pad

    final_h, final_w = sq_hw, sq_hw
    sample_h, sample_w = min(h, w), min(h, w)
    sample_h, sample_w = int(sample_p*sample_h/100), int(sample_p*sample_w/100)

    k_size = blur*2+1
    assert k_size > 0, ":("

    res = img[h//2-sample_h//2: h//2-sample_h//2+sample_h,
              w//2-sample_w//2: w//2-sample_w//2+sample_w]

    res = cv2.resize(res, (final_w, final_h),
                     interpolation=cv2.INTER_CUBIC)

    res = cv2.GaussianBlur(res, (k_size, k_size), 0)

    r_h, r_w, _ = res.shape
    assert r_h >= h and r_w >= w, "result image smaller"
    res[r_h//2-h//2: r_h//2-h//2+h,
        r_w//2-w//2: r_w//2-w//2+w] = img

    cv2.imwrite("sq_"+args.image, res)


if __name__ == '__main__':
    main()
