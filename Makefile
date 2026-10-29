# Kritva Actuator: repository checks and helpers (Kritva Makefile standard, kritva-program v2/planning/standards/MAKEFILE_STANDARD.md)
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

PYTHON ?= python3
ROOT   := $(CURDIR)

# A target is documented by `name: ## text` on its rule line; `##@ Name` starts a help group.
# An unimplemented gate exits 3 (NOT_IMPLEMENTED). It is never a pass.
.DEFAULT_GOAL := help
.PHONY: help

##@ Help
help: ## Show this list
	@awk 'BEGIN { FS = ":.*##"; printf "\nUsage: make <target> [VAR=value ...]\n" } \
	  /^##@/ { g = substr($$0, 5); next } \
	  /^[a-zA-Z0-9_.-]+:[^=].*##/ { if (g != "") { printf "\n%s\n", g; g = "" }; sub(/^ +/, "", $$2); printf "  %-24s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

##@ Checks
.PHONY: check check-docs check-links check-readme check-trace check-bom check-calcs check-manifest check-submodules check-status
check: check-docs check-links check-trace check-bom check-calcs check-manifest check-submodules check-status  ## Run all documentation, traceability, BOM and calculation checks

check-docs: ## Check KA- document headers and revision history
	$(PYTHON) scripts/validation/check_docs.py --root $(ROOT)

check-links: ## Check relative Markdown links
	$(PYTHON) scripts/validation/check_links.py --root $(ROOT)

check-readme: ## Check README.md against the Kritva README standard (structure, metadata, local links)
	$(PYTHON) scripts/validation/check_readme.py README.md --root $(ROOT)

check-trace: ## Validate the traceability CSV against requirement IDs
	$(PYTHON) scripts/validation/check_traceability.py --root $(ROOT) --summary

check-bom: ## Validate mechanical and electrical BOM CSV schema
	$(PYTHON) scripts/bom/check_bom.py --root $(ROOT)

check-calcs: ## Regression-check actuator_sizing.py and its consistency with the calculation documents
	$(PYTHON) scripts/validation/check_calcs.py --root $(ROOT)

check-manifest: ## Check planning/v2/MIGRATION_MANIFEST.csv against the working tree
	$(PYTHON) scripts/validation/check_manifest.py --root $(ROOT)

check-submodules: ## Check the four-submodule layout (.gitmodules, URLs without credentials)
	$(PYTHON) scripts/integration/check_submodules.py --root $(ROOT)

check-status: ## Validate status/status.json (kritva-program status schema 2.0) against status/tasks.csv
	$(PYTHON) scripts/status/gen_status.py --root $(ROOT) --check

##@ Tools
.PHONY: bom-summary calc clean
bom-summary: ## Print BOM cost totals by milestone and category
	$(PYTHON) scripts/bom/bom_summary.py --root $(ROOT) --markdown

calc: ## Run the mechanical sizing calculations
	@if [ -f mechanical/common-sizing/actuator_sizing.py ]; then \
		$(PYTHON) mechanical/common-sizing/actuator_sizing.py; \
	else echo "mechanical/common-sizing/actuator_sizing.py not present"; fi

clean: ## Remove Python caches (__pycache__ and *.pyc)
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	find . -name "*.pyc" -delete


##@ Gates (unimplemented gates exit 3)
.PHONY: docs-check
docs-check: check-docs check-links ## Document headers and relative links

define not_implemented
	@echo "NOT_IMPLEMENTED: $(1) has no tests yet; this is not a pass"; exit 3
endef

.PHONY: lint
lint: ## Static analysis and lint (NOT_IMPLEMENTED: exits 3)
	$(call not_implemented,lint)

.PHONY: test-unit
test-unit: ## Unit tests (NOT_IMPLEMENTED: exits 3)
	$(call not_implemented,test-unit)

.PHONY: test-integration
test-integration: ## Integration tests (NOT_IMPLEMENTED: exits 3)
	$(call not_implemented,test-integration)

.PHONY: test-regression
test-regression: ## Regression tests (NOT_IMPLEMENTED: exits 3)
	$(call not_implemented,test-regression)

.PHONY: test
test: ## All tests (NOT_IMPLEMENTED: exits 3)
	$(call not_implemented,test)

.PHONY: acceptance
acceptance: ## Acceptance gate (NOT_IMPLEMENTED: exits 3)
	$(call not_implemented,acceptance)

##@ Git
.PHONY: git_sync
git_sync: ## Switch to main, fast-forward from origin, prune, delete merged local branches
	@git switch main
	@git pull --ff-only --prune
	@git branch --format='%(refname:short)' | grep -vx main | xargs -r git branch -d
	@git log --oneline -3
