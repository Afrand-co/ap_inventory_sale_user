# Inventory Access for Sales Users

This Odoo module allows users with the "Sales / User: Own Documents Only" role to access inventory reporting functionality.

## Features

- Grants read-only access to stock data for Sales users
- Makes Inventory → Reporting → Stock menu accessible to Sales users
- Provides read-only views for:
  - Stock quantities (Stock on Hand)
  - Stock moves
  - Stock pickings

## Installation

1. Place this module in your Odoo addons directory
2. Update the module list in Odoo
3. Install the module

## Usage

After installation, users with the "Sales / User: Own Documents Only" role will be able to:

1. Access the Inventory → Reporting → Stock menu
2. View stock quantities, moves, and picking operations in read-only mode
3. Navigate through stock locations and products

## Technical Details

### Security Access Rules

The module adds read-only access to the following models for the `sales_team.group_sale_salesman` group:
- `stock.quant` (Stock quantities)
- `stock.move` (Stock moves)
- `stock.picking` (Stock pickings)
- `product.product` (Products)
- `stock.location` (Stock locations)

### Menu Access

Sales users can access stock data through existing Odoo menus and reporting features. The module provides model-level access that enables viewing stock information through standard Odoo interfaces.

### Read-Only Views

Custom views ensure that Sales users can only view data and cannot create, edit, or delete stock records.

## Testing

To test the module:

1. Create a user with "Sales / User: Own Documents Only" role
2. Log in as that user
3. Verify access to Inventory → Reporting → Stock menu
4. Confirm that stock data is visible in read-only mode
5. Attempt to edit/create/delete stock records (should be prevented)
