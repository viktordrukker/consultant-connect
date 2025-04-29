# Consultant Connect - MVP User Stories (Iteration-Based)

This document outlines the user stories for the Minimum Viable Product (MVP), structured by development iteration based on technical dependencies.

## MVP Goal:
Deliver a functional platform enabling seekers to find, book, have a session with, pay, and rate consultants, validating the core value proposition and transaction loop.

---

### Iteration 1: Backend Foundation & Core Models

*   **Tech Story 1.1: Project Setup**
    *   **As a** Developer, **I want to** initialize the FastAPI backend project structure, configure basic settings (like environment variables), and set up dependency management (e.g., using Poetry or pip), **so that** we have a clean foundation for backend development.
*   **Tech Story 1.2: Database & Migrations Setup**
    *   **As a** Developer, **I want to** configure the PostgreSQL database connection, integrate SQLAlchemy for ORM, and set up Alembic for database migrations, **so that** we can manage database schema changes reliably.
*   **US 1.3: Define User Model**
    *   **As a** Developer, **I want to** define the `User` database model (SQLAlchemy) and corresponding Pydantic schema, including fields like `id`, `email`, `hashed_password`, `first_name`, `last_name`, `role` (Seeker/Consultant), `is_active`, `created_at`, `updated_at`, **so that** we can store basic user information.
*   **US 1.4: Define Profile Model**
    *   **As a** Developer, **I want to** define the `ConsultantProfile` model and schema, linked to the `User` model, including fields like `headline`, `bio`, `expertise_tags` (e.g., JSON or array), `hourly_rate`, `created_at`, `updated_at`, **so that** consultants can store their professional details.
*   **US 1.5: Define Availability Model**
    *   **As a** Developer, **I want to** define the `AvailabilitySlot` model and schema, linked to a Consultant `User`, including fields like `start_time`, `end_time`, `is_booked`, `created_at`, `updated_at`, **so that** consultants can specify when they are available.
*   **US 1.6: Define Booking Model**
    *   **As a** Developer, **I want to** define the `Booking` model and schema, linking a Seeker `User`, a Consultant `User`, and an `AvailabilitySlot`, including fields like `status` (e.g., requested, confirmed, completed, cancelled), `session_start_time`, `session_end_time`, `payment_intent_id` (from Stripe), `created_at`, `updated_at`, **so that** session bookings can be tracked.
*   **US 1.7: Define Rating Model**
    *   **As a** Developer, **I want to** define the `Rating` model and schema, linked to a `Booking`, a Seeker `User` (rater), and a Consultant `User` (rated), including fields like `score` (1-5), `comment` (optional), `created_at`, **so that** seekers can rate completed sessions.
*   **Tech Story 1.8: Implement Basic Authentication Logic**
    *   **As a** Developer, **I want to** implement backend functions for password hashing (e.g., using passlib), password verification, JWT token generation upon login, and JWT token decoding/validation for protected endpoints, **so that** user authentication can be handled securely.

---

### Iteration 2: Backend APIs - Profile & Discovery

*   **US 2.1: API - Register User**
    *   **As a** Frontend Developer (or API consumer), **I want** an API endpoint (`POST /users/register`) that accepts user registration details (name, email, password, role), validates them, creates a new `User` record, and returns user info and a JWT token, **so that** new users can sign up.
*   **US 2.2: API - Login User**
    *   **As a** Frontend Developer, **I want** an API endpoint (`POST /users/login`) that accepts email and password, verifies credentials, and returns user info and a JWT token upon success, **so that** registered users can log in.
*   **US 2.3: API - Get Current User**
    *   **As a** Frontend Developer, **I want** a protected API endpoint (`GET /users/me`) that uses the JWT token to identify and return the currently logged-in user's details, **so that** the frontend knows who is logged in.
*   **US 2.4: API - Create/Update Consultant Profile**
    *   **As a** Consultant (via Frontend), **I want** a protected API endpoint (`PUT /consultants/me/profile`) that allows me to create or update my `ConsultantProfile` (headline, bio, expertise, rate), **so that** I can manage my professional details.
*   **US 2.5: API - Get Consultant Profile**
    *   **As a** User (via Frontend), **I want** an API endpoint (`GET /consultants/{consultant_id}/profile`) to retrieve the public profile details of a specific consultant, **so that** seekers can view consultant information.
*   **US 2.6: API - Set Availability Slots**
    *   **As a** Consultant (via Frontend), **I want** a protected API endpoint (`POST /consultants/me/availability`) that allows me to define my available time slots for a given period, **so that** seekers know when I can be booked.
*   **US 2.7: API - Get Consultant Availability**
    *   **As a** Seeker (via Frontend), **I want** an API endpoint (`GET /consultants/{consultant_id}/availability`) to retrieve the available (not booked) time slots for a specific consultant, **so that** I can see when they can be booked.
*   **US 2.8: API - List Consultants (Directory)**
    *   **As a** Seeker (via Frontend), **I want** an API endpoint (`GET /consultants`) that returns a paginated list of all public consultants, including their name, headline, and average rating, **so that** I can browse the directory.
*   **US 2.9: API - Search Consultants**
    *   **As a** Seeker (via Frontend), **I want** the `GET /consultants` endpoint to accept query parameters (e.g., `?search=keyword`) to filter the list based on keywords matching name, headline, or expertise, **so that** I can find relevant consultants.

---

### Iteration 3: Backend APIs - Booking & Payment Setup

*   **US 3.1: API - Request Booking**
    *   **As a** Seeker (via Frontend), **I want** a protected API endpoint (`POST /bookings`) that allows me to request a booking for a specific consultant's available time slot, **so that** I can initiate the booking process.
*   **US 3.2: API - View My Bookings (Seeker & Consultant)**
    *   **As a** Logged-in User (via Frontend), **I want** a protected API endpoint (`GET /bookings/me`) that returns a list of my bookings (as seeker or consultant), filterable by status (requested, confirmed, completed, etc.), **so that** I can track my sessions.
*   **US 3.3: API - Accept/Decline Booking**
    *   **As a** Consultant (via Frontend), **I want** protected API endpoints (`POST /bookings/{booking_id}/accept` and `POST /bookings/{booking_id}/decline`) to change the status of a requested booking, **so that** I can manage incoming requests.
*   **Tech Story 3.4: API - Setup Stripe Payment Method (Seeker)**
    *   **As a** Seeker (via Frontend), **I want** an API endpoint (`POST /payments/setup-intent`) that creates a Stripe SetupIntent, returning its client secret, **so that** the frontend can use Stripe Elements to securely collect and save my payment method details with Stripe.
*   **Tech Story 3.5: API - Create Stripe Connect Account (Consultant)**
    *   **As a** Consultant (via Frontend), **I want** an API endpoint (`POST /payments/connect-account`) that creates a Stripe Connect Express account for me and returns an account link, **so that** I can complete Stripe onboarding to receive payouts.
*   **Tech Story 3.6: API - Handle Stripe Webhooks (Basic)**
    *   **As a** Developer, **I want** a webhook endpoint (`POST /webhooks/stripe`) to receive basic events from Stripe (e.g., payment method setup success, Connect account updated), **so that** the platform can react to payment-related events (specific handling TBD).

---

### Iteration 4: Backend APIs - Session & Payment Execution

*   **US 4.1: API - Start Session**
    *   **As a** Seeker or Consultant (via Frontend), **I want** a protected API endpoint (`POST /bookings/{booking_id}/start`) that marks the booking status as 'in_progress' and records the actual start time, **so that** the session officially begins.
*   **US 4.2: API - End Session**
    *   **As a** Seeker or Consultant (via Frontend), **I want** a protected API endpoint (`POST /bookings/{booking_id}/end`) that marks the booking status as 'completed', records the end time, calculates the duration, and triggers payment processing if duration > 10 mins, **so that** the session is formally concluded and payment is handled.
*   **Tech Story 4.3: Implement Payment Pre-authorization**
    *   **As a** Developer, **I want** the "Accept Booking" logic (US 3.3) to create and confirm a Stripe PaymentIntent with `capture_method=manual` for the consultant's rate, using the seeker's saved payment method, storing the `payment_intent_id` on the booking, **so that** funds are guaranteed before the session.
*   **Tech Story 4.4: Implement Payment Capture**
    *   **As a** Developer, **I want** the "End Session" logic (US 4.2) to check the session duration. If > 10 mins, it should capture the previously authorized PaymentIntent via the Stripe API, **so that** the seeker is charged for the successful session.
*   **Tech Story 4.5: Implement Commission & Payout Logic**
    *   **As a** Developer, **I want** the payment capture logic (or a subsequent process triggered by webhook) to calculate the platform commission, and initiate a Stripe transfer to the consultant's connected account for the remaining amount, **so that** the consultant gets paid.
*   **US 4.6: API - Submit Rating**
    *   **As a** Seeker (via Frontend), **I want** a protected API endpoint (`POST /bookings/{booking_id}/rating`) that allows me to submit a star rating (1-5) for a completed booking, **so that** I can provide feedback on the session.
*   **Tech Story 4.7: Calculate Average Rating**
    *   **As a** Developer, **I want** the consultant profile retrieval logic (US 2.5) to calculate and include the consultant's average rating based on submitted `Rating` records, **so that** seekers can see their reputation.

---

### Iteration 5: Frontend Foundation & Authentication

*   **Tech Story 5.1: Initialize Frontend Project**
    *   **As a** Developer, **I want to** initialize the React project using Vite, set up basic project structure (components, pages, services), install necessary libraries (e.g., React Router, Axios/fetch), and configure basic styling (e.g., CSS Modules or Tailwind CSS), **so that** we have a foundation for frontend development.
*   **Tech Story 5.2: Implement Routing**
    *   **As a** Developer, **I want to** set up client-side routing using React Router, defining routes for public pages (Login, Register) and protected pages (Dashboard, Profile, etc.), **so that** users can navigate the single-page application.
*   **Tech Story 5.3: Implement Auth State Management**
    *   **As a** Developer, **I want to** implement global state management (e.g., Context API or Zustand/Redux Toolkit) to store user authentication status (logged in/out) and JWT token, persisting the token (e.g., in localStorage), **so that** the UI can react to auth state and make authenticated API calls.
*   **US 5.4: Build Registration Page**
    *   **As a** New User, **I want** a registration page with fields for name, email, password, confirmation, and role selection, which calls the registration API (US 2.1) upon submission, handles errors, and redirects upon success, **so that** I can sign up.
*   **US 5.5: Build Login Page**
    *   **As a** Registered User, **I want** a login page with fields for email and password, which calls the login API (US 2.2) upon submission, handles errors, and redirects to a protected area upon success, **so that** I can log in.
*   **US 5.6: Implement Logout Functionality**
    *   **As a** Logged-in User, **I want** a logout button (e.g., in a header) that clears the auth state/token and redirects to the login page, **so that** I can log out.
*   **Tech Story 5.7: Implement Protected Routes**
    *   **As a** Developer, **I want to** create a mechanism (e.g., a wrapper component) that checks the auth state and redirects unauthenticated users away from protected routes to the login page, **so that** only logged-in users can access certain areas.

---

### Iteration 6: Frontend - Profile & Discovery

*   **US 6.1: Build Consultant Directory Page**
    *   **As a** Seeker, **I want** a page that calls the list consultants API (US 2.8), displays the list of consultants (Name, Headline, Avg Rating), includes a search bar that calls the search API (US 2.9) to filter the list, and makes each consultant entry clickable, **so that** I can find consultants.
*   **US 6.2: Build Consultant Profile View Page**
    *   **As a** Seeker, **I want** a page that displays the full details of a specific consultant (fetched via US 2.5), including Name, Headline, Bio, Expertise, Rate, and Average Rating, and their available time slots (fetched via US 2.7), **so that** I can evaluate them and see when they are available.
*   **US 6.3: Build Consultant Profile Edit Page**
    *   **As a** Consultant, **I want** a protected page with forms to edit my profile details (Headline, Bio, Expertise, Rate) and save changes via the API (US 2.4), **so that** I can manage my public information.
*   **US 6.4: Build Availability Management UI**
    *   **As a** Consultant, **I want** a UI (e.g., a calendar view or date/time pickers) on my profile edit page or dashboard to define my available time slots and submit them via the API (US 2.6), **so that** I can set my schedule.

---

### Iteration 7: Frontend - Booking & Session Flow

*   **US 7.1: Implement Booking Request UI**
    *   **As a** Seeker, **I want** to be able to select an available time slot on the consultant's profile view page (US 6.2) and click a "Request Booking" button that calls the booking request API (US 3.1), **so that** I can book a session.
*   **US 7.2: Build Booking Dashboard (Seeker)**
    *   **As a** Seeker, **I want** a protected dashboard page that lists my bookings (fetched via US 3.2), showing consultant name, time, and status (Requested, Confirmed, Completed, etc.), **so that** I can track my sessions.
*   **US 7.3: Build Booking Dashboard (Consultant)**
    *   **As a** Consultant, **I want** a protected dashboard page that lists bookings requested/confirmed with me (fetched via US 3.2), showing seeker name, time, and status, with buttons to Accept/Decline pending requests (calling US 3.3), **so that** I can manage my bookings.
*   **US 7.4: Build Basic Session Page**
    *   **As a** Seeker or Consultant, **I want** a simple page for confirmed bookings that shows participant names, the scheduled time, a visible 10-minute countdown timer upon starting, and "Start Session" / "End Session" buttons (calling US 4.1 / US 4.2), **so that** we can manage the session lifecycle.
*   **US 7.5: Implement Rating Submission UI**
    *   **As a** Seeker, **I want** to see a prompt (e.g., on my dashboard or after ending a session) for completed sessions, allowing me to select a 1-5 star rating and submit it via the API (US 4.6), **so that** I can rate the consultant.

---

### Iteration 8: Frontend - Payment Integration

*   **US 8.1: Implement Seeker Payment Method Setup**
    *   **As a** Seeker, **I want** a section (e.g., in my profile settings) where I can use a Stripe Elements form (using the client secret from US 3.4) to securely add/update my credit card details, **so that** I can pay for sessions.
*   **US 8.2: Implement Consultant Stripe Onboarding Flow**
    *   **As a** Consultant, **I want** a prompt (e.g., in my profile settings or dashboard) with a button that calls the API (US 3.5) and redirects me to Stripe's Connect Onboarding flow, **so that** I can securely provide my details to Stripe for receiving payouts.
*   **Tech Story 8.3: Handle Booking Pre-authorization Flow**
    *   **As a** Seeker, **when** my booking request is accepted by the consultant, **I want** the system to attempt pre-authorization using my saved payment method (triggered by backend logic Tech Story 4.3), and see the booking status update to "Confirmed" if successful, or receive an error notification if payment fails, **so that** the booking is secured.
*   **US 8.4: Display Basic Transaction History (Seeker)**
    *   **As a** Seeker, **I want** a section displaying a list of my past payments for completed sessions (basic info like consultant, date, amount), **so that** I can track my spending. (Requires a simple backend API endpoint).
*   **US 8.5: Display Basic Payout History (Consultant)**
    *   **As a** Consultant, **I want** a section displaying a list of my past payouts received (basic info like session date, amount received after commission), **so that** I can track my earnings. (Requires a simple backend API endpoint).

---
