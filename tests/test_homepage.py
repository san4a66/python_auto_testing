import time

import pytest

from pom.homepage_nav import HomePageNav


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_nav_links(self):
        homepage_nav = HomePageNav(self.driver)
        for index in range(12):
            homepage_nav.get_nav_links()[index].click()



