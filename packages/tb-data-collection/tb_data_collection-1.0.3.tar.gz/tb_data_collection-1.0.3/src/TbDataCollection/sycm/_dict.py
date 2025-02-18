class Home:
    overall__overview = {
        '支付金额': 'payAmt',
        '店铺客户数': 'shopCustomer',
        '平均停留时长': 'stayTime',
        '支付买家数': 'payByrCnt',
        '老客复购率': 'hasPurchaseUbyCntRate',
        '老客复购人数': 'payOldByrCnt',
        '老客复购金额': 'olderPayAmt',
        '支付子订单数': 'subPayOrdSubCnt',
        '支付件数': 'payItmCnt',
        '浏览量': 'pv',
        '成功退款金额': 'rfdSucAmt',
        '净支付金额': 'netPaymentAmount',
        '加购件数': 'cartCnt',
        '加购人数': 'cartByrCnt',
        '商品收藏人数': 'cltItmCnt',
        '咨询率': 'consultRate',
        '旺旺人工响应时长': 'wwReplyManualAvgTimeLen',
        '24小时揽收及时率': 'gotInTime24hRate',
        '物流到货时长': 'avgSignTimeHh',
        '退款处理时长': 'rfdFinshDur',
        '成功退款率': 'sucRefundRate',
        '全站推广花费': 'admCostFamtQzt',
        '关键词推广花费': 'p4pExpendAmt',
        '精准人群推广花费': 'cubeAmt',
        '智能场景花费': 'adStrategyAmt',
        '淘宝客佣金': 'tkExpendAmt',
    }


class Goods:
    goods360__goods_info = {
        '主图链接': 'pictUrl',
        '商品标题': 'title',
        '商品链接': 'detailUrl',
        '分类ID': 'categoryId',
    }
    goods360__sale__overview = {
        '商品访客数': 'itmUv',
        '商品微详情访客数': 'miniDetailUv',
        '商品浏览量': 'itmPv',
        '平均停留时长': 'itmStayTime',
        '商品详情页跳出率': 'itmBounceRate',
        '商品加购人数': 'itemCartByrCnt',
        '商品加购件数': 'itemCartCnt',
        '商品收藏人数': 'itemCltByrCnt',
        '访问收藏转化率': 'visitCltRate',
        '访问加购转化率': 'visitCartRate',
        '下单买家数': 'crtByrCnt',
        '下单件数': 'crtItmQty',
        '下单金额': 'crtAmt',
        '下单转化率': 'crtRate',
        '支付买家数': 'payByrCnt',
        '支付件数': 'payItmCnt',
        '支付金额': 'payAmt',
        '支付转化率': 'payRate',
        '聚划算支付金额': 'juPayAmt',
        '支付新买家数': 'newPayByrCnt',
        '支付老买家数': 'payOldByrCnt',
        '老买家支付金额': 'olderPayAmt',
        '访客平均价值': 'uvAvgValue',
    }
    goods360__flow__detail = {
        '访客数': 'uv',
        '下单买家数': 'crtByrCnt',
        '下单转化率': 'crtRate',
        '浏览量': 'pv',
        '店内跳转人数': 'jpSelfUv',
        '跳出本店人数': 'jpUv',
        '收藏人数': 'cltCnt',
        '加购人数': 'cartByrCnt',
        '支付金额': 'payAmt',
        '支付件数': 'payItmCnt',
        '支付买家数': 'payByrCnt',
        '支付转化率': 'payRate',
        '直接支付买家数': 'directPayByrCnt',
        '收藏商品-支付买家数': 'cltItmPayByrCnt',
        '粉丝支付买家数': 'fansPayByrCnt',
        '加购商品-支付买家数': 'ordItmPayByrCnt',
    }


class Dictionary:
    home = Home()
    goods = Goods()
