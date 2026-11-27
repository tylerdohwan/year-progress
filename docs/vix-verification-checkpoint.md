# VIX verification checkpoint — 2026-11-27

- market.html blob a3c95917e72fdfeaa434eec000772e50ae60854e: CBOE:VIX Mini Symbol Overview.
- vix-diagnostics.html blob 281aca988f00ed01a211679c8362ae6c519d06fb: Mini Symbol Overview and Symbol Info; iframe insertion is not quote verification.
- TradingView official data FAQ https://www.tradingview.com/widget-docs/faq/data/ states that symbols restricted to TradingView cannot be displayed in any widget timeframe; paid personal plans do not change widget entitlements.
- Official North America widget market list https://www.tradingview.com/widget-docs/markets/north-america/ lists Cboe One delayed stocks and CFE delayed futures, but does not explicitly list Cboe VIX cash index. Do not infer support from symbol existence.
- Published diagnostics URL could not be accessed by the web retrieval environment; this is not evidence of a failed public deployment or failed quote rendering.
- Next gate: user screenshot of https://tylerdohwan.github.io/year-progress/vix-diagnostics.html or authorized browser rendering. If restricted, investigate separately licensed alternatives; do not scrape or redistribute quotes.
- DGS30 repository observation 2026-11-24, 5.30%; published JSON parity unverified. Existing collector workflow includes direct Pages deployment. Production files unchanged.
