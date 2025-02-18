from time import sleep

from DrissionPage._pages.mix_tab import MixTab


def pick__custom_date(date: str, page: MixTab):
    """选择自定义日期"""

    day_btn = page.ele('t:button@@text()=日', timeout=3)
    if not day_btn:
        raise RuntimeError('未找到 [日] 按钮')

    year, month, day = date.split('-')

    day_btn.click(by_js=True)

    selector_header = page.ele('c:div.d-datepicker-header', timeout=3)
    year_btn, month_btn = selector_header.eles(
        'c:div.d-datepicker-header-main h6.d-text', timeout=1
    )[:2]

    curr_year = year_btn.text.strip()[:-1]
    curr_month = month_btn.text.strip()[:-1]

    selector_header_icons = selector_header.eles('c:span.d-icon.d-clickable', timeout=1)

    def click__arrow_btn(src: str, dst: str, prev_index: int, next_index: int):
        v_number = int(dst)
        curr_v_number = int(src)
        diff_count = abs(curr_v_number - v_number)
        arrow_btn = None
        if curr_v_number > v_number:
            arrow_btn = selector_header_icons[prev_index]
        else:
            arrow_btn = selector_header_icons[next_index]

        for _ in range(diff_count):
            arrow_btn.click(by_js=True)
            sleep(0.3)

    if curr_year != year:
        click__arrow_btn(year, curr_year, -1, 0)

    if curr_month != month:
        click__arrow_btn(month, curr_month, -2, 1)

    day_number = int(day)
    day_btn = page.ele(
        f't:div@@class^d-datepicker-cell-main@@text()={day_number}', timeout=1
    )
    if not day_btn:
        raise RuntimeError(f'日期选择器中未找到日期 {day}')

    day_btn.click(by_js=True)
