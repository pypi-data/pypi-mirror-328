
from ..mixins.auth import AuthType

class XMonitorClient(BaseAPIClient, AuthMixin, RateLimitMixin):
    """XMonitor API client"""
    
    def __init__(self, config_path: str = "config.yml", use_proxy: bool = True):
        """Initialize XMonitor client"""
        super().__init__("x_monitor", config_path, use_proxy)
        
        # Setup authentication and rate limits
        self.setup_auth(AuthType.API_KEY)

        self.setup_rate_limits(self.ENDPOINTS)