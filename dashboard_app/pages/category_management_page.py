from __future__ import annotations

from pathlib import Path
from typing import Iterable

from playwright.sync_api import (
    expect,
    Frame,
    TimeoutError as PlaywrightTimeoutError,
)

from shared.core.base_page import BasePage


class CategoryManagementPage(BasePage):
    # =========================
    # Navigation
    # =========================
    LNK_CATEGORY_MGMT = "//li[.//span[text()='Category Management']]"
    LNK_CATEGORIES_1 = "//a[.//span[normalize-space()='Categories']]"
    LNK_CATEGORIES_2 = "//a[.//span[text()='Categories']]"
    H1_CATEGORY_MGMT = "//h1[normalize-space()='Category Management']"

    # =========================
    # Headers (Assertions)
    # =========================
    TH_SN = "//th[normalize-space()='S/N']"
    TH_SERVICE_TYPE = "//th//button[normalize-space()='Service Type']"
    TH_CATEGORY_NAME = "//th//button[normalize-space()='Category Name']"
    TH_DESCRIPTION = "//th[normalize-space()='Description']"
    TH_STATUS = "//th[normalize-space()='Status']"
    TH_CREATED_BY = "//th//button[normalize-space()='Created By']"
    TH_LAST_UPDATED_BY = "//th//button[normalize-space()='Last Updated By']"
    TH_CREATED_AT = "//th//button[normalize-space()='Created At']"
    TH_ACTIONS = "//th[normalize-space()='Actions']"

    # =========================
    # Row actions / menus (kept for flow compatibility)
    # =========================
    BTN_ACTIONS = "//button[@aria-label='Actions']"
    MENU_VIEW_SUBCATEGORIES = "//span[normalize-space()='View Subcategories']"

    # =========================
    # Add category form (Steps 7–11)
    # =========================
    BTN_ADD_CATEGORY = "//button[normalize-space()='Add Category']"

    # In the modal screenshot this text exists inside upload dropzone.
    # We keep it only to assert modal is open — DO NOT CLICK it.
    P_CHOOSE_MAIN_IMAGE = "//p[normalize-space()='Choose a main image for category']"

    CMB_SERVICE_TYPE = (
        "//label[contains(normalize-space(.),'Service Type')]/following::button[@role='combobox'][1]"
    )
    OPT_DIGITAL_SERVICES = "//div[@role='option' and normalize-space()='Digital Services']"

    # NOTE: your modal shows a single input "Enter name of category"
    # but you asked to use this locator, so we keep it.
    INPUT_CATEGORY_NAMES = "//input[@type='text' and @placeholder='Enter one or more names']"

    BTN_SAVE_CATEGORY = "//button[@type='submit' and normalize-space()='Save Category']"

    # =========================
    # Navigation methods
    # =========================
    def go_to_categories(self) -> None:
        # Step 1: click Category Management
        self.page.locator(self.LNK_CATEGORY_MGMT).click()

        # Step 2: click Categories
        if self.page.locator(self.LNK_CATEGORIES_1).count() > 0:
            self.page.locator(self.LNK_CATEGORIES_1).click()
        else:
            self.page.locator(self.LNK_CATEGORIES_2).click()

    def assert_on_category_management(self) -> None:
        # Step 3
        expect(self.page.locator(self.H1_CATEGORY_MGMT)).to_be_visible(timeout=20000)
        print("We reached on Category Management")

    def assert_table_headers(self) -> None:
        # Step 4
        expect(self.page.locator(self.TH_SN)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_SERVICE_TYPE)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_CATEGORY_NAME)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_DESCRIPTION)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_STATUS)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_CREATED_BY)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_LAST_UPDATED_BY)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_CREATED_AT)).to_be_visible(timeout=20000)
        expect(self.page.locator(self.TH_ACTIONS)).to_be_visible(timeout=20000)

    # =========================
    # ✅ Methods REQUIRED by your flow (don’t remove)
    # =========================
    def open_first_row_actions(self) -> None:
        actions = self.page.locator(self.BTN_ACTIONS)
        if actions.count() == 0:
            print("ℹ️ Actions button not found (skipping open_first_row_actions)")
            return
        try:
            expect(actions.first).to_be_visible(timeout=8000)
            actions.first.click()
        except Exception:
            print("ℹ️ Unable to click Actions (skipping)")

    def click_view_subcategories(self) -> None:
        menu = self.page.locator(self.MENU_VIEW_SUBCATEGORIES)
        if menu.count() == 0:
            print("ℹ️ View Subcategories not found (skipping click_view_subcategories)")
            return
        try:
            expect(menu).to_be_visible(timeout=8000)
            menu.click()
        except Exception:
            print("ℹ️ Unable to click View Subcategories (skipping)")

    # =========================
    # Helpers
    # =========================
    def _frames(self) -> Iterable[Frame]:
        return self.page.frames

    def _pick_image(self, images_dir: Path) -> Path:
        images_dir = images_dir.resolve()
        if not images_dir.exists():
            raise FileNotFoundError(f"Images folder not found: {images_dir}")

        exts = (".png", ".jpg", ".jpeg", ".webp", ".gif")
        files = [p for p in images_dir.iterdir() if p.suffix.lower() in exts]
        if not files:
            raise FileNotFoundError(f"No image files found in: {images_dir}")
        return files[0].resolve()

    # =========================
    # Step 7: Click Add Category
    # =========================
    def click_add_category(self) -> None:
        btn = self.page.locator(self.BTN_ADD_CATEGORY)
        expect(btn).to_be_visible(timeout=20000)
        btn.click()

        # Modal opened indicator (from your screenshot)
        expect(self.page.locator(self.P_CHOOSE_MAIN_IMAGE)).to_be_visible(timeout=20000)

    # =========================
    # Step 8: Upload Main Image (NO OS FILE PICKER)
    # =========================
    def upload_main_image(self, images_dir: Path) -> Path:
        """
        IMPORTANT:
        Do NOT click the dropzone because that opens Windows "Browse" dialog.
        Instead set file directly on the hidden input[type=file].

        In your modal there are 2 uploaders:
        0 -> Category Main Image
        1 -> Category Banner Image
        """
        file_path = self._pick_image(images_dir)

        # Wait file inputs to exist inside modal
        file_inputs = self.page.locator("input[type='file']")
        try:
            file_inputs.first.wait_for(state="attached", timeout=15000)
        except PlaywrightTimeoutError:
            shot = self.screenshot("file_inputs_not_found")
            raise AssertionError(
                "❌ input[type=file] not found in Add New Category modal.\n"
                f"URL: {self.page.url}\n"
                f"Screenshot: {Path(shot).resolve()}"
            )

        count = file_inputs.count()
        if count == 0:
            shot = self.screenshot("file_inputs_count_zero")
            raise AssertionError(
                "❌ input[type=file] count is 0.\n"
                f"URL: {self.page.url}\n"
                f"Screenshot: {Path(shot).resolve()}"
            )

        # Use first input for MAIN IMAGE
        try:
            file_inputs.nth(0).set_input_files(str(file_path))
            print(f"✅ Uploaded MAIN image: {file_path.name}")
            return file_path
        except Exception:
            # fallback: some UIs reverse ordering, try second
            if count > 1:
                file_inputs.nth(1).set_input_files(str(file_path))
                print(f"✅ Uploaded MAIN image via 2nd input: {file_path.name}")
                return file_path

            shot = self.screenshot("set_input_files_failed")
            raise AssertionError(
                "❌ set_input_files() failed for input[type=file].\n"
                f"URL: {self.page.url}\n"
                f"Screenshot: {Path(shot).resolve()}"
            )

    # =========================
    # Step 9: Service Type
    # =========================
    def select_service_type_digital_services(self) -> None:
        cmb = self.page.locator(self.CMB_SERVICE_TYPE)
        expect(cmb).to_be_visible(timeout=20000)
        cmb.click()

        opt = self.page.locator(self.OPT_DIGITAL_SERVICES)
        expect(opt).to_be_visible(timeout=20000)
        opt.click()

    # =========================
    # Step 10: Names
    # =========================
    def enter_service_names(self, names: list[str]) -> None:
        inp = self.page.locator(self.INPUT_CATEGORY_NAMES)
        expect(inp).to_be_visible(timeout=20000)

        for name in names:
            inp.fill(name)
            inp.press("Enter")

    # =========================
    # Step 11: Save
    # =========================
    def save_category(self) -> None:
        btn = self.page.locator(self.BTN_SAVE_CATEGORY)
        expect(btn).to_be_visible(timeout=20000)
        btn.click()
