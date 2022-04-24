from collections import defaultdict

"""
sales_summary_per_day

{
    "20211209": {
        "123": {
            "payment_count": 1,
            "total_amount": 7000,
        },
        "647": {
            "payment_count": 2,
            "total_amount": 8000,
        }
    },
    "20211210": {
        "126": {
            "payment_count": 1,
            "total_amount": 7000,
        },
        "649": {
            "payment_count": 2,
            "total_amount": 8000,
        }
    },
}
"""

if __name__ == "__main__":
    sales_summary_per_day = defaultdict(lambda: defaultdict(str))

    test_a = defaultdict(list)

    test_a["a"].append(1)
    print(test_a)

    # sales_summary_per_day["20211209"] = {
    #     "123": {
    #         "payment_count": 1,
    #         "total_amount": 7000,
    #     },
    # }
    try:
        sales_summary_per_day["20211209"]["123"]["payment_count"] += 1
        sales_summary_per_day["20211209"]["123"]["total_amount"] += 1
    except TypeError:
        sales_summary_per_day["20211209"]["123"] = {
            "payment_count": 1,
            "total_amount": 7000,
        }

    print(sales_summary_per_day)

    test = defaultdict(str)
    test["123"] = {"123": {"123": 123}}
    print(test)
