# Kritva Actuator - repository checks and helpers
# Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

PYTHON ?= python3
ROOT   := $(CURDIR)

.PHONY: help check check-docs check-links check-trace check-bom check-calcs check-manifest check-submodules bom-summary calc clean

help:  ## List available targets
	@echo "Kritva Actuator make targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-14s %s\n", $$1, $$2}'

check: check-docs check-links check-trace check-bom check-calcs check-manifest check-submodules  ## Run all documentation, traceability, BOM and calculation checks

check-docs:  ## Check KA- document headers and revision history
	$(PYTHON) scripts/validation/check_docs.py --root $(ROOT)

check-links:  ## Check relative Markdown links
	$(PYTHON) scripts/validation/check_links.py --root $(ROOT)

check-trace:  ## Validate the traceability CSV against requirement IDs
	$(PYTHON) scripts/validation/check_traceability.py --root $(ROOT) --summary

check-bom:  ## Validate mechanical and electrical BOM CSV schema
	$(PYTHON) scripts/bom/check_bom.py --root $(ROOT)

check-calcs:  ## Regression-check actuator_sizing.py and its consistency with the calculation documents
	$(PYTHON) scripts/validation/check_calcs.py --root $(ROOT)

check-manifest:  ## Check planning/v2/MIGRATION_MANIFEST.csv against the working tree
	$(PYTHON) scripts/validation/check_manifest.py --root $(ROOT)

check-submodules:  ## Check the four-submodule layout (.gitmodules, URLs without credentials)
	$(PYTHON) scripts/integration/check_submodules.py --root $(ROOT)

bom-summary:  ## Print BOM cost totals by milestone and category
	$(PYTHON) scripts/bom/bom_summary.py --root $(ROOT) --markdown

calc:  ## Run the mechanical sizing calculations
	@if [ -f mechanical/calculations/actuator_sizing.py ]; then \
		$(PYTHON) mechanical/calculations/actuator_sizing.py; \
	else echo "mechanical/calculations/actuator_sizing.py not present"; fi

clean:  ## Remove Python caches and generated reports
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	find . -name "*.pyc" -delete
