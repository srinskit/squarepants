#! python3
import cv2
import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image",
        help="Path to image file"
    )

    parser.add_argument(
        "-s",
        "--shape",
        choices=["original", "round"],
        default="original",
        help="Shaped of the inner image"
    )

    parser.add_argument(
        "-p",
        "--padding",
        default=40,
        type=int,
        help="Minimum padding around the inner image"
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Run in debug mode"
    )

    args = parser.parse_args()
    img = cv2.imread(args.image, cv2.IMREAD_COLOR)

    h, w, _ = img.shape
    pad, sample_p, blur = args.padding, 90, 70

    if args.shape == "round":
        sq_hw = min(h, w) + 2*pad
    elif args.shape == "original":
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
    assert r_h == final_h and r_w == final_w, ":(("

    if args.shape == "round":
        r = min(h, w)//2
        img = img[h//2-r: h//2+r, w//2-r:w//2+r]
        mask = np.zeros((2*r, 2*r), np.uint8)
        mask = cv2.circle(mask, (r, r), r, 255, cv2.FILLED)

        img = cv2.bitwise_and(img, img, mask=mask)
        x = res[r_h//2-r: r_h//2+r,
                r_w//2-r: r_w//2+r]

        x = cv2.bitwise_and(x, x, mask=cv2.bitwise_not(mask))
        img += x
        res[r_h//2-r: r_h//2+r,
            r_w//2-r: r_w//2+r] = img
    elif args.shape == "original":
        res[r_h//2-h//2: r_h//2-h//2+h,
            r_w//2-w//2: r_w//2-w//2+w] = img

    if args.debug:
        cv2.imshow("res", res)
        cv2.waitKey(0)
    cv2.imwrite("sq_"+args.image, res)


if __name__ == '__main__':
    main()
