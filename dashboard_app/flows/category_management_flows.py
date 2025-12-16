from __future__ import annotations

from pathlib import Path
from dashboard_app.pages.category_management_page import CategoryManagementPage


class CategoryManagementFlows:
    def __init__(self, page):
        self.page = page
        self.cm = CategoryManagementPage(page)

    def add_categories_with_image_and_service_type(self) -> None:
        self.cm.go_to_categories()
        self.cm.assert_on_category_management()
        self.cm.assert_table_headers()

        self.cm.open_first_row_actions()
        self.cm.click_view_subcategories()

        self.cm.click_add_category()

        ROOT = Path(__file__).resolve().parents[2]  # project root
        images_dir = ROOT / "testdata" / "images"
        chosen = self.cm.upload_main_image(images_dir)
        print(f"✅ Uploaded image: {chosen.name}")

        self.cm.select_service_type_digital_services()

        names = [
            "Electricity & Water Bills",
            "Insurance",
            "Airtime",
            "Cashin",
            "Cable TV",
            "Corporate Payments",
            "Events & Tickets",
            "Products & Services",
            "Tax & Government",
            "Data & Internet",
        ]
        self.cm.enter_service_names(names)

        self.cm.save_category()
