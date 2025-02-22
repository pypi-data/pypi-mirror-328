## [$(date '+%Y-%m-%d')] Refactor Supabase Client to use psycopg3
- Changes Made: Updated `supabase_mcp/client.py` to use `psycopg` (version 3) and `psycopg_pool.ConnectionPool`.  Modified imports, connection pool initialization, and the `readonly_query` method to use the new library and its features (autocommit, context managers). Updated exception handling.
- Feedback: User requested to switch to `psycopg` 3 and `psycopg_pool`.
- Lessons: `psycopg` 3 offers a cleaner API and built-in connection pooling, simplifying the code and improving maintainability.  Autocommit simplifies transaction management for read-only queries. Context managers ensure proper resource cleanup.
- Next Steps:  Update dependencies in `pyproject.toml` and `requirements.txt` (if it exists) to reflect the change to `psycopg[binary,pool]`. Update tests to ensure compatibility with the new library. 

## [2024-08-23] Versioning Issue with PyPI

- Changes Made:
    - Updated `pyproject.toml` to use dynamic versioning from `supabase_mcp/_version.py`.
    - Created/updated `supabase_mcp/_version.py` with the correct version number.
- Feedback:
    - The previous build failed because the version string included a local version identifier, which is not allowed by PyPI.
- Lessons:
    - Local version identifiers are not allowed in public releases on PyPI.
    - It's better to use dynamic versioning to avoid hardcoding the version in `pyproject.toml`.
    - `hatch-vcs` can be configured to generate PEP 440 compliant versions, but it's more complex.  For now, dynamic versioning from a separate file is a good solution.
- Next Steps:
    - Consider investigating `hatch-vcs` configuration to generate compliant versions automatically.
    - Ensure the version number is updated in `supabase_mcp/_version.py` for each new release.
- Operating Policy:
    - Prioritize fixing build/publish issues immediately.
    - Favor dynamic versioning to keep the version in a single, easily updated location.
    - When encountering a new tool (like hatch-vcs), spend a little extra time up front to understand the configuration options, to avoid issues later. 