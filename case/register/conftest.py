import pytest
from common.connect_mysql import execute_sql


@pytest.fixture()
def delete_user():
    delete_sql = 'DELETE FROM auth_user WHERE username = "test_123";'
    execute_sql(delete_sql)
    yield
    print("用例之后执行的！")