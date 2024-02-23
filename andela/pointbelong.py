"""
function area(x1, y1, x2, y2, x3, y3) {
    return Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
}
function pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq) {
    let mainArea = area(x1, y1, x2, y2, x3, y3)
    let a1 = area(xp, yp, x2, y2, x3, y3)
    let a2 = area(x1, y1, xp, yp, x3, y3)
    let a3 = area(x1, y1, x2, y2, xp, yp,)

    let b1 = area(xq, yq, x2, y2, x3, y3)
    let b2 = area(x1, y1, xq, yq, x3, y3)
    let b3 = area(x1, y1, x2, y2, xq, yq,)
    if (mainArea == 0) {
        return 0;
    }
    let isP = (mainArea == a1 + a2 + a3)
    let isQ = (mainArea == b1 + b2 + b3)
    if (isP && !isQ) {
        return 1;
    }
    if (isQ && !isP) {
        return 2;
    }
    if (isQ && isP) {
        return 3;
    } if (!isP && !isQ) {
        return 4;
    }
}
"""

def get_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def point_belong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    main_area = get_area(x1, y1, x2, y2, x3, y3)

    area_one = get_area(xp, yp, x2, y2, x3, y3)
    area_two = get_area(x1, y1, xp, yp, x3, y3)
    area_three = get_area(x1, y1, x2, y2, xp, yp)

    b1 = get_area(xq, yq, x2, y2, x3, y3)
    b2 = get_area(x1, y1, xq, yq, x3, y3)
    b3 = get_area(x1, y1, x2, y2, xq, yq)

    if main_area == 0:
        return 0

    isP = main_area == area_one + area_two + area_three
    isQ = main_area == b1 + b2 + b3

    if isP and not isQ:
        return 1
    
    if isQ and not isP:
        return 2

    if isQ and isP:
        return 3

    return 4


if __name__ == '__main__':
    print(point_belong(4,2,3,4,2,3,7,1,3,1))