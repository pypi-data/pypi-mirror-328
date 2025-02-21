from typing import Optional

from dmtapi.models.account_model import TraderInfo
from dmtapi.models.trade_model import TradeSetup
from dmtapi.req import RequestMaker


class AccountInfoApi(RequestMaker):
    def __init__(self, api_key: str, api_base_url: str):
        super().__init__(api_base_url)
        self.api_key = api_key

    async def info(
        self,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> TraderInfo:
        """
        Retrieve information about a specific trading account.

        Args:
            access_token (Optional[str]): Account access token. Required if login and server are not provided.
            login (Optional[str]): Account login. Required if access_token is not provided.
            server (Optional[str]): Trading server. Required if access_token is not provided.
            api_key (Optional[str]): Override default API key.

        Returns:
            TraderInfo: Object containing account information.

        Raises:
            ValueError: If neither access_token nor both login and server are provided.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.get(
            path="/account/info",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
        )

        return TraderInfo(**r)

    async def all(self, api_key: Optional[str] = None) -> list[TraderInfo]:
        """
        Retrieve information about all available trading accounts.

        Args:
            api_key (Optional[str]): Override default API key.

        Returns:
            list[TraderInfo]: List of objects containing account information.
        """
        r = await self.get(path="/account/all", api_key=api_key or self.api_key)

        return [TraderInfo(**i) for i in r]


class TradeApi(RequestMaker):
    def __init__(self, api_key: str, api_base_url: str):
        super().__init__(api_base_url)
        self.api_key = api_key

    async def open(
        self,
        setup: TradeSetup,
        access_token: str,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> list[dict]:
        """
        Open a new trade based on the provided setup.

        Args:
            setup (TradeSetup): Trade configuration including symbol, volume, direction, etc.
            access_token (str): Account access token.
            login (int): Account login number.
            server (str): Trading server.
            api_key (Optional[str]): Override default API key.

        Returns:
            list[dict]: List of trade results.
            If you have multiple tp it returns multiple trades as MT5 doesn't support more than one tp on a trade.
            So it splits the volume and opens multiple trades with the same entry, sl and tp.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.post(
            path="/trade/open",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
            data=setup.model_dump_json(),
        )

        return r

    async def close(
        self,
        ticket: int,
        volume: float = None,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Close an open position by ticket number. Enter volume for partial close.

        Args:
            ticket (int): Ticket number of the position to close.
            volume (float): Volume to close. If not provided, the entire position will be closed.
            access_token (Optional[str]): Account access token. Required if login and server are not provided.
            login (Optional[str]): Account login. Required if access_token is not provided.
            server (Optional[str]): Trading server. Required if access_token is not provided.
            api_key (Optional[str]): Override default API key.

        Returns:
            dict: Response from the server.

        Raises:
            ValueError: If it fails to close the position.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.get(
            path="/trade/close",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
            params={"ticket": ticket, "volume": str(volume)},
        )

        return r

    async def cancel(
        self,
        ticket: int,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Cancel a pending order by ticket number

        Args:
            ticket (int): Ticket number of the pending order to cancel.
            access_token (Optional[str]): Account access token. Required if login and server are not provided.
            login (Optional[str]): Account login. Required if access_token is not provided.
            server (Optional[str]): Trading server. Required if access_token is not provided.
            api_key (Optional[str]): Override default API key.

        Returns:
            dict: Response from the server.

        Raises:
            ValueError: If it fails to cancel the pending order.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.get(
            path="/trade/cancel",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
            params={"ticket": str(ticket)},
        )

        return r


class SymbolApi(RequestMaker):
    def __init__(self, api_key: str, api_base_url: str):
        super().__init__(api_base_url)
        self.api_key = api_key

    async def price(
        self,
        symbol: str,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Get the current price of a symbol.

        Args:
            symbol (str): Symbol name.
            access_token (Optional[str]): Account access token. Required if login and server are not provided.
            login (Optional[str]): Account login. Required if access_token is not provided.
            server (Optional[str]): Trading server. Required if access_token is not provided.
            api_key (Optional[str]): Override default API key.

        Returns:
            dict: Symbol price information.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.get(
            path="/symbol/price",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
            params={"symbol": symbol},
        )

        return r

    async def info(
        self,
        symbol: str,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Get information about a symbol.

        Args:
            symbol (str): Symbol name.
            access_token (Optional[str]): Account access token. Required if login and server are not provided.
            login (Optional[str]): Account login. Required if access_token is not provided.
            server (Optional[str]): Trading server. Required if access_token is not provided.
            api_key (Optional[str]): Override default API key.

        Returns:
            dict: Symbol information.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.get(
            path="/symbol/info",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
            params={"symbol": symbol},
        )

        return r

    async def all(
        self,
        access_token: Optional[str] = None,
        login: Optional[int] = None,
        server: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Get information about all available symbols.

        Args:
            access_token (Optional[str]): Account access token. Required if login and server are not provided.
            login (Optional[str]): Account login. Required if access_token is not provided.
            server (Optional[str]): Trading server. Required if access_token is not provided.
            api_key (Optional[str]): Override default API key.

        Returns:
            list[dict]: List of symbol information.
        """
        if not access_token and (not login or not server):
            raise ValueError("Access token or login and server must be provided")

        r = await self.get(
            path="/symbol/all",
            access_token=access_token,
            login=login,
            server=server,
            api_key=api_key or self.api_key,
        )

        return r


class DMTAPI:
    """
    Main class for interacting with the DMT trading API.

    This class provides methods to manage trading accounts and execute trades.

    Args:
        api_key (str): The API key for authentication.
    """

    def __init__(self, api_key: str, api_base_url: str):
        self.api_key = api_key
        self.account = AccountInfoApi(self.api_key, api_base_url)
        self.trade = TradeApi(self.api_key, api_base_url)
        self.symbol = SymbolApi(self.api_key, api_base_url)
