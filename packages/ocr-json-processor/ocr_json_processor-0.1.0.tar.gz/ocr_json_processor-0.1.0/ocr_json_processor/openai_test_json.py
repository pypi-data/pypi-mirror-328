orix_resp = {
    "is_balance_sheet_present": "Yes",
    "balance_sheet": {
        "assets": {
            "cash": [{
                "1120 - Operating Trust Account": {
                    "value": "-4960.59",
                    "page_number": 3,
                }
            }]
        },
        "liabilities": {
            "accounts_payable": [{
                "2200 - Accounts Payable": {"value": "32238.11", "page_number": 4},
                "2405 - Due to RichSmith Management": {
                    "value": "134274.22",
                    "page_number": 4,
                },
            }]
        },
    },
    "income_statement": {
        "revenue_income": {
            "apartment_revenue": [{
                "Rent Income-Tenant": {"value": "519,619.00", "page_number": 5}
            }],
            "gain_loss_to_lease":[{
                "Gain (Loss) to Lease": {"value": "-87,907.15", "page_number": 5}
            }],
        }
    },
}

tvs_resp = {
    "risk": {
        "vendor_name": {
            "value": "EMERGENCY KITS INDIA PRIVATE LIMITED ",
            "page_number": "4",
            "exact_value": "EMERGENCY KITS INDIA PRIVATE LIMITED ",
        },
         "vendor_name": {
            "value": "EMERGENCY KITS INDIA PRIVATE LIMITED ",
            "page_number": "4",
            "exact_value": "EMERGENCY KITS INDIA PRIVATE LIMITED ",
        }
    },
    "yearly_financial_metrics": [
        {
            "vendor_name": {
                "value": "Vendor Name",
                "page_number": "4",
                "exact_value": "exact value/text present in the extracted text",
            },
            "vendor_name": {
                "value": "Vendor Name",
                "page_number": "4",
                "exact_value": "exact value/text present in the extracted text",
            }
        }
    ]
}

essent_resp = {
        'borrower_name': {
                "value": "Kamala Harris",
                "page_number": "1",
                "exact_value": "Kamala Harris"
            },
            'borrower_name': {
                "value": "Kamala Harris",
                "page_number": "1",
                "exact_value": "Kamala Harris"
            }
            
            }