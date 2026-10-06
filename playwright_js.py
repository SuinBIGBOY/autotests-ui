from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
        wait_until='networkidle'
        )

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')

    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        'New Text 1'
    )
    page.wait_for_timeout(3000)