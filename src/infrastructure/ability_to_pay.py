def max_monthly_fee(income, size, extra_expenses):
    income = income - extra_expenses
    if income < 1610:
        return 0
    elif 1610 <= income < 1799:
        if size == 1:
            return 40
        elif size > 1:
            return 0
    elif 1799 <= income < 1988:
        if size == 1:
            return 48
        elif size > 1:
            return 0
    elif 1988 <= income < 2178:
        if size == 1:
            return 56
        elif size > 1:
            return 0
    elif 2178 <= income < 2367:
        if size == 1:
            return 65
        elif size == 2:
            return 40
    elif 2367 <= income < 2556:
        if size == 1:
            return 74
        elif size == 2:
            return 48
        elif size > 2:
            return 0
    elif 2556 <= income < 2745:
        if size == 1:
            return 84
        elif size == 2:
            return 56
        elif size > 2:
            return 0
    elif 2745 <= income < 2934:
        if size == 1:
            return 95
        elif size == 2:
            return 65
        elif size == 3:
            return 40
        elif size > 3:
            return 0
    elif 2934 <= income < 3123:
        if size == 1:
            return 106
        elif size == 2:
            return 74
        elif size == 3:
            return 48
        elif size > 3:
            return 0
    elif 3123 <= income < 3313:
        if size == 1:
            return 118
        elif size == 2:
            return 84
        elif size == 3:
            return 56
        elif size > 3:
            return 0
    elif 3313 <= income < 3502:
        if size == 1:
            return 131
        elif size == 2:
            return 95
        elif size == 3:
            return 65
        elif size == 4:
            return 40
        elif size > 4:
            return 0
    elif 3502 <= income < 3691:
        if size == 1:
            return 144
        elif size == 2:
            return 106
        elif size == 3:
            return 74
        elif size == 4:
            return 48
        elif size > 4:
            return 0
    elif 3691 <= income < 3880:
        if size == 1:
            return 157
        elif size == 2:
            return 118
        elif size == 3:
            return 84
        elif size == 4:
            return 56
        elif size > 4:
            return 0
    elif 3880 <= income < 4069:
        if size == 1:
            return 171
        elif size == 2:
            return 131
        elif size == 3:
            return 95
        elif size == 4:
            return 65
        elif size == 5:
            return 40
        elif size > 5:
            return 0
    elif 4069 <= income < 4258:
        if size == 1:
            return 186
        elif size == 2:
            return 144
        elif size == 3:
            return 106
        elif size == 4:
            return 74
        elif size == 5:
            return 48
        elif size > 5:
            return 0
    elif 4258 <= income < 4448:
        if size == 1:
            return 202
        elif size == 2:
            return 157
        elif size == 3:
            return 118
        elif size == 4:
            return 84
        elif size == 5:
            return 56
        elif size > 5:
            return 0
    elif 4448 <= income < 4637:
        if size == 1:
            return 218
        elif size == 2:
            return 171
        elif size == 3:
            return 131
        elif size == 4:
            return 95
        elif size == 5:
            return 65
        elif size == 6:
            return 40
        elif size > 6:
            return 0
    elif 4637 <= income < 4826:
        if size == 1:
            return 235
        elif size == 2:
            return 186
        elif size == 3:
            return 144
        elif size == 4:
            return 106
        elif size == 5:
            return 74
        elif size == 6:
            return 48
        elif size > 6:
            return 0
    elif 4826 <= income < 5015:
        if size == 1:
            return 252
        elif size == 2:
            return 202
        elif size == 3:
            return 157
        elif size == 4:
            return 118
        elif size == 5:
            return 84
        elif size == 6:
            return 56
        elif size > 6:
            return 0
    elif 5015 <= income < 5204:
        if size == 1:
            return 270
        elif size == 2:
            return 218
        elif size == 3:
            return 171
        elif size == 4:
            return 131
        elif size == 5:
            return 95
        elif size == 6:
            return 65
        elif size == 7:
            return 40
        elif size > 7:
            return 0
    elif 5204 <= income < 5393:
        if size == 1:
            return 288
        elif size == 2:
            return 235
        elif size == 3:
            return 186
        elif size == 4:
            return 144
        elif size == 5:
            return 106
        elif size == 6:
            return 74
        elif size == 7:
            return 48
        elif size > 7:
            return 0
    elif 5393 <= income < 5583:
        if size == 1:
            return 307
        elif size == 2:
            return 252
        elif size == 3:
            return 202
        elif size == 4:
            return 157
        elif size == 5:
            return 118
        elif size == 6:
            return 84
        elif size == 7:
            return 56
        elif size > 7:
            return 0
    elif 5583 <= income < 5772:
        if size == 1:
            return 327
        elif size == 2:
            return 270
        elif size == 3:
            return 218
        elif size == 4:
            return 171
        elif size == 5:
            return 131
        elif size == 6:
            return 95
        elif size == 7:
            return 65
        elif size == 8:
            return 40
        elif size > 8:
            return 0
    elif 5772 <= income < 5961:
        if size == 1:
            return 347
        elif size == 2:
            return 288
        elif size == 3:
            return 235
        elif size == 4:
            return 186
        elif size == 5:
            return 144
        elif size == 6:
            return 106
        elif size == 7:
            return 74
        elif size == 8:
            return 48
        elif size > 8:
            return 0
    elif 5961 <= income < 6150:
        if size == 1:
            return 368
        elif size == 2:
            return 307
        elif size == 3:
            return 252
        elif size == 4:
            return 202
        elif size == 5:
            return 157
        elif size == 6:
            return 118
        elif size == 7:
            return 84
        elif size == 8:
            return 56
        elif size > 8:
            return 0
    elif 6150 <= income < 6339:
        if size == 1:
            return 390
        elif size == 2:
            return 327
        elif size == 3:
            return 270
        elif size == 4:
            return 218
        elif size == 5:
            return 171
        elif size == 6:
            return 131
        elif size == 7:
            return 95
        elif size == 8:
            return 65
        elif size >= 9:
            return 40
    elif 6339 <= income < 6528:
        if size == 1:
            return 412
        elif size == 2:
            return 347
        elif size == 3:
            return 288
        elif size == 4:
            return 235
        elif size == 5:
            return 186
        elif size == 6:
            return 144
        elif size == 7:
            return 106
        elif size == 8:
            return 74
        elif size >= 9:
            return 48
    elif 6528 <= income < 6718:
        if size == 1:
            return 435
        elif size == 2:
            return 368
        elif size == 3:
            return 307
        elif size == 4:
            return 252
        elif size == 5:
            return 202
        elif size == 6:
            return 157
        elif size == 7:
            return 118
        elif size == 8:
            return 84
        elif size >= 9:
            return 56
    elif 6718 <= income < 6907:
        if size == 1:
            return 458
        elif size == 2:
            return 390
        elif size == 3:
            return 327
        elif size == 4:
            return 270
        elif size == 5:
            return 218
        elif size == 6:
            return 171
        elif size == 7:
            return 131
        elif size == 8:
            return 95
        elif size >= 9:
            return 65
    elif 6907 <= income < 7096:
        if size == 1:
            return 482
        elif size == 2:
            return 412
        elif size == 3:
            return 347
        elif size == 4:
            return 288
        elif size == 5:
            return 235
        elif size == 6:
            return 186
        elif size == 7:
            return 144
        elif size == 8:
            return 106
        elif size >= 9:
            return 74
    elif 7096 <= income < 7285:
        if size == 1:
            return 507
        elif size == 2:
            return 435
        elif size == 3:
            return 368
        elif size == 4:
            return 307
        elif size == 5:
            return 252
        elif size == 6:
            return 202
        elif size == 7:
            return 157
        elif size == 8:
            return 118
        elif size >= 9:
            return 84
    elif 7285 <= income < 7474:
        if size == 1:
            return 532
        elif size == 2:
            return 458
        elif size == 3:
            return 390
        elif size == 4:
            return 327
        elif size == 5:
            return 270
        elif size == 6:
            return 218
        elif size == 7:
            return 171
        elif size == 8:
            return 131
        elif size >= 9:
            return 95
    elif 7474 <= income < 7663:
        if size == 1:
            return 558
        elif size == 2:
            return 482
        elif size == 3:
            return 412
        elif size == 4:
            return 347
        elif size == 5:
            return 288
        elif size == 6:
            return 235
        elif size == 7:
            return 186
        elif size == 8:
            return 144
        elif size >= 9:
            return 106
    elif 7663 <= income < 7853:
        if size == 1:
            return 584
        elif size == 2:
            return 507
        elif size == 3:
            return 435
        elif size == 4:
            return 368
        elif size == 5:
            return 307
        elif size == 6:
            return 252
        elif size == 7:
            return 202
        elif size == 8:
            return 157
        elif size >= 9:
            return 117
    elif 7853 <= income < 8042:
        if size == 1:
            return 611
        elif size == 2:
            return 532
        elif size == 3:
            return 458
        elif size == 4:
            return 390
        elif size == 5:
            return 327
        elif size == 6:
            return 270
        elif size == 7:
            return 218
        elif size == 8:
            return 171
        elif size >= 9:
            return 129
    elif 8042 <= income < 8231:
        if size == 1:
            return 639
        elif size == 2:
            return 558
        elif size == 3:
            return 482
        elif size == 4:
            return 412
        elif size == 5:
            return 347
        elif size == 6:
            return 288
        elif size == 7:
            return 235
        elif size == 8:
            return 186
        elif size >= 9:
            return 142
    elif 8231 <= income < 8420:
        if size == 1:
            return 667
        elif size == 2:
            return 584
        elif size == 3:
            return 507
        elif size == 4:
            return 435
        elif size == 5:
            return 368
        elif size == 6:
            return 307
        elif size == 7:
            return 252
        elif size == 8:
            return 202
        elif size >= 9:
            return 157
    elif 8420 <= income < 8609:
        if size == 1:
            return 695
        elif size == 2:
            return 611
        elif size == 3:
            return 532
        elif size == 4:
            return 458
        elif size == 5:
            return 390
        elif size == 6:
            return 327
        elif size == 7:
            return 270
        elif size == 8:
            return 218
        elif size >= 9:
            return 171
    elif 8609 <= income < 8798:
        if size == 1:
            return 725
        elif size == 2:
            return 639
        elif size == 3:
            return 558
        elif size == 4:
            return 482
        elif size == 5:
            return 412
        elif size == 6:
            return 347
        elif size == 7:
            return 288
        elif size == 8:
            return 235
        elif size >= 9:
            return 186
    elif 8798 <= income < 8988:
        if size == 1:
            return 755
        elif size == 2:
            return 667
        elif size == 3:
            return 584
        elif size == 4:
            return 507
        elif size == 5:
            return 435
        elif size == 6:
            return 368
        elif size == 7:
            return 307
        elif size == 8:
            return 252
        elif size >= 9:
            return 202
    elif 8988 <= income < 9177:
        if size == 1:
            return 786
        elif size == 2:
            return 695
        elif size == 3:
            return 611
        elif size == 4:
            return 532
        elif size == 5:
            return 458
        elif size == 6:
            return 390
        elif size == 7:
            return 327
        elif size == 8:
            return 270
        elif size >= 9:
            return 218
    elif 9177 <= income < 9366:
        if size == 1:
            return 817
        elif size == 2:
            return 725
        elif size == 3:
            return 639
        elif size == 4:
            return 558
        elif size == 5:
            return 482
        elif size == 6:
            return 412
        elif size == 7:
            return 347
        elif size == 8:
            return 288
        elif size >= 9:
            return 235
    elif 9366 <= income < 9555:
        if size == 1:
            return 849
        elif size == 2:
            return 755
        elif size == 3:
            return 667
        elif size == 4:
            return 584
        elif size == 5:
            return 507
        elif size == 6:
            return 435
        elif size == 7:
            return 368
        elif size == 8:
            return 307
        elif size >= 9:
            return 252
    elif 9555 <= income < 9744:
        if size == 1:
            return 881
        elif size == 2:
            return 786
        elif size == 3:
            return 695
        elif size == 4:
            return 611
        elif size == 5:
            return 532
        elif size == 6:
            return 458
        elif size == 7:
            return 390
        elif size == 8:
            return 327
        elif size >= 9:
            return 270
    elif 9744 <= income < 9933:
        if size == 1:
            return 914
        elif size == 2:
            return 817
        elif size == 3:
            return 725
        elif size == 4:
            return 639
        elif size == 5:
            return 558
        elif size == 6:
            return 482
        elif size == 7:
            return 412
        elif size == 8:
            return 347
        elif size >= 9:
            return 288
    elif 9933 <= income < 10123:
        if size == 1:
            return 948
        elif size == 2:
            return 849
        elif size == 3:
            return 755
        elif size == 4:
            return 667
        elif size == 5:
            return 584
        elif size == 6:
            return 507
        elif size == 7:
            return 435
        elif size == 8:
            return 368
        elif size >= 9:
            return 307
    elif 10123 <= income < 10312:
        if size == 1:
            return 982
        elif size == 2:
            return 881
        elif size == 3:
            return 786
        elif size == 4:
            return 695
        elif size == 5:
            return 611
        elif size == 6:
            return 532
        elif size == 7:
            return 458
        elif size == 8:
            return 390
        elif size >= 9:
            return 327
    elif 10312 <= income < 10501:
        if size == 1:
            return 1017
        elif size == 2:
            return 914
        elif size == 3:
            return 817
        elif size == 4:
            return 725
        elif size == 5:
            return 639
        elif size == 6:
            return 558
        elif size == 7:
            return 482
        elif size == 8:
            return 412
        elif size >= 9:
            return 347
    elif 10501 <= income < 10690:
        if size == 1:
            return 1052
        elif size == 2:
            return 948
        elif size == 3:
            return 849
        elif size == 4:
            return 755
        elif size == 5:
            return 667
        elif size == 6:
            return 584
        elif size == 7:
            return 507
        elif size == 8:
            return 435
        elif size >= 9:
            return 368
    elif 10690 <= income < 10879:
        if size == 1:
            return 1088
        elif size == 2:
            return 982
        elif size == 3:
            return 881
        elif size == 4:
            return 786
        elif size == 5:
            return 695
        elif size == 6:
            return 611
        elif size == 7:
            return 532
        elif size == 8:
            return 458
        elif size >= 9:
            return 390
    elif 10879 <= income < 11068:
        if size == 1:
            return 1125
        elif size == 2:
            return 1017
        elif size == 3:
            return 914
        elif size == 4:
            return 817
        elif size == 5:
            return 725
        elif size == 6:
            return 639
        elif size == 7:
            return 558
        elif size == 8:
            return 482
        elif size >= 9:
            return 412
    elif 11068 <= income < 11258:
        if size == 1:
            return 1162
        elif size == 2:
            return 1052
        elif size == 3:
            return 948
        elif size == 4:
            return 849
        elif size == 5:
            return 755
        elif size == 6:
            return 667
        elif size == 7:
            return 584
        elif size == 8:
            return 507
        elif size >= 9:
            return 435
    elif 11258 <= income < 11447:
        if size == 1:
            return 1200
        elif size == 2:
            return 1088
        elif size == 3:
            return 982
        elif size == 4:
            return 881
        elif size == 5:
            return 786
        elif size == 6:
            return 695
        elif size == 7:
            return 611
        elif size == 8:
            return 532
        elif size >= 9:
            return 458
    elif 11447 <= income < 11636:
        if size == 1:
            return 1239
        elif size == 2:
            return 1125
        elif size == 3:
            return 1017
        elif size == 4:
            return 914
        elif size == 5:
            return 817
        elif size == 6:
            return 725
        elif size == 7:
            return 639
        elif size == 8:
            return 558
        elif size >= 9:
            return 482
    elif 11636 <= income < 11825:
        if size == 1:
            return 1278
        elif size == 2:
            return 1162
        elif size == 3:
            return 1052
        elif size == 4:
            return 948
        elif size == 5:
            return 849
        elif size == 6:
            return 755
        elif size == 7:
            return 667
        elif size == 8:
            return 584
        elif size >= 9:
            return 507
    elif 11825 <= income < 12014:
        if size == 1:
            return 1317
        elif size == 2:
            return 1200
        elif size == 3:
            return 1088
        elif size == 4:
            return 982
        elif size == 5:
            return 881
        elif size == 6:
            return 786
        elif size == 7:
            return 695
        elif size == 8:
            return 611
        elif size >= 9:
            return 532
    elif income >= 12014:
        if size == 1:
            return 1358
        elif size == 2:
            return 1239
        elif size == 3:
            return 1125
        elif size == 4:
            return 1017
        elif size == 5:
            return 914
        elif size == 6:
            return 817
        elif size == 7:
            return 725
        elif size == 8:
            return 639
        elif size >= 9:
            return 558
