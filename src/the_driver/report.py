from the_driver.models import RepoData, ScanResult, ReviewResult


def generate_report(
    repo_data: RepoData,
    scan_result: ScanResult,
    review_result: ReviewResult,
    candidate: str | None = None,
    repo_url: str | None = None,
) -> str:
    raise NotImplementedError("Phase 2: Business Domain")
