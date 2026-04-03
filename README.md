# Finance Data Processing and Access Control Backend

A production-grade financial management system built with Django REST Framework. Developed with a focus on data integrity, role-based security, and architectural clarity.

## Key Features
- **Service Layer Architecture**: Decouples business logic from API views for maximum maintainability.
- **Role-Based Access Control (RBAC)**: Strict permission enforcement for Admin, Analyst, and Viewer roles.
- **Soft Delete System**: Financial records are never lost; they are flagged as deleted to maintain audit trails.
- **Audit Logging**: Comprehensive `created_at` and `updated_at` timestamps for every transaction.
- **High Performance Dashboard**: Aggregated statistics and category breakdowns powered by database-level indexing and optimized ORM queries.

## Architecture & Design Decisions

### Why a Service Layer?
Standard Django patterns often lead to "fat" models or "fat" views. By introducing a Service Layer (`finance/services/`), we encapsulate the business logic in plain Python classes. This makes the system easier to test and extend.

### Data Safety (Soft Delete)
In financial systems, accidental deletion is a critical risk. We implemented a custom `Manager` and `QuerySet` that overrides the default `.delete()` behavior, ensuring records are only hidden from the UI but remain in the database for auditing.

### Security (JWT + RBAC)
We use stateless JWT authentication via `djangorestframework-simplejwt`. Permissions are enforced using custom DRF classes:
- **Admin**: Full CRUD on all transactions and users.
- **Analyst**: View access to all transactions + Full Dashboard summaries.
- **Viewer**: View access to transactions only.

---

## 🛠 Setup Instructions

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/Siddharth-Nama/zorvyn_assignment.git
   ```

2. **Environment Setup**:
   - Create a `.env` file in the `backend/` folder (Refer to `backend/.env` for keys).
   - Install dependencies:
     ```bash
     pip install -r backend/requirements.txt
     ```

3. **Database Migration**:
   ```bash
   python backend/manage.py migrate
   ```

4. **Run Server**:
   ```bash
   python backend/manage.py runserver
   ```

---

## API Summary

| Endpoint | Method | Role Access | Description |
| :--- | :--- | :--- | :--- |
| `/api/accounts/token/` | POST | Anonymous | Get JWT tokens |
| `/api/finance/transactions/` | GET | All | List all active transactions |
| `/api/finance/transactions/` | POST | Admin | Create a new transaction |
| `/api/dashboard/summary/` | GET | Admin / Analyst | View financial summary stats |

---

## Tradeoffs & Assumptions
- **Single Currency**: Currently supports a single currency (Decimal precision) for simplicity.
- **No Caching**: For this assessment, we prioritized direct DB query performance via indexing over cache-layer complexity.
- **Mock Token Setup**: Local development uses a simple secret key; for production, this should be rotated via a vault.
