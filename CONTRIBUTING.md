<!--
SPDX-FileCopyrightText: © 2024 University of Bristol
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Contributing to the BriCS application site documentation

## Found a mistake in the application site docs?

If you've seen something in the documentation that contains a typo, is misleading, or doesn't work correctly, then please feel free to report it.
First check the [list of issues][issues] to see if it's already been reported.
If you have a GitHub account, then you can [raise an issue][new-issue] directly to let us know and we will aim to resolve it.
If you do not have a GitHub account but have an account on one of our systems, then you can raise a ticket as usual through our [support desk][support].

## Want to contribute directly?

If you want to make a change directly to the documentation, we welcome your contribution.

In general, all changes should be reviewed for suitability to include in the documentation.

For any minor changes (e.g. fixing typos, rewording a paragraph, adding extra detail to existing documentation), the change can be submitted directly as a PR and be checked in a lightweight review by members of the BriCS team.

For more substantial changes (e.g. new pages or sections, restructuring existing pages, removal of pages or sections), we recommend [opening an issue][new-issue] to discuss the proposed change with the BriCS team first.
This will avoid you investing effort in a PR, which may be rejected or require substantial revision because it does not fit within the scope and structure of the documentation.
It will also help avoid duplication of work where multiple individuals may be working on similar contributions.

Before submitting a PR, please check this list to help with a speedy review:
- The PR should be made against the `main` branch.
- All contributions must be licensed as [CC BY-SA 4.0][cc-by-sa] with a [`SPDX-FileCopyrightText`][reuse-spec] line added if needed.
- Text must be written in British English.
- Ensure that the documentation builds successfully on your computer with no errors.
  You can check this with `mkdocs build --strict`.
- Try to limit the use of jargon where it may hinder understanding by a wider audience.
- Prefer writing each sentence in markdown on its own line, as it aids in tracking changes later and avoids any line getting too long.
- All images should be added with alt text, like `![A photo of a man smoking a cigar in front of some large chains](isambard.jpeg)` including explicitly any text visible in the image.

[new-issue]: https://github.com/isambard-sc/apply.isambard.ac.uk/issues/new
[issues]: https://github.com/isambard-sc/apply.isambard.ac.uk/issues/
[support]: https://support.isambard.ac.uk
[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[reuse-spec]: https://reuse.software/spec-3.2/
