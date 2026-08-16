# Security Policy

## Supported versions

Security fixes are provided for the latest published Protocol version. During the pre-1.0 phase, maintainers may also patch the immediately preceding minor line when a safe compatibility-preserving fix is possible.

## Reporting a vulnerability

Do not open a public issue for an undisclosed vulnerability. Use GitHub private vulnerability reporting for `compaos/compaos-protocol` when available. If that channel is unavailable, email [protocol@compaos.ai](mailto:protocol@compaos.ai) with the subject `SECURITY: Compaos Protocol vulnerability report`.

Do not include secrets or unnecessary personal, customer, or production data. If email encryption is required, request a secure exchange channel before sending sensitive reproduction material.

Reports should include the affected version, object or rule, impact, reproduction steps, and any proposed mitigation. Maintainers should acknowledge a complete report within five business days and coordinate disclosure after a fix or mitigation is available.

## Scope

Security-sensitive areas include authority bypass, forged lifecycle events, canonicalization or hash divergence, replay, counter misuse, unsafe schema ambiguity, and incorrect conformance claims. Vulnerabilities in a specific implementation belong to that implementation unless they arise from the Protocol or its reference code.
