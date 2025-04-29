# Consultant Connect - Development Roadmap (MVP Focus)

This roadmap outlines the planned iterations for building the Minimum Viable Product (MVP), focusing on a technically logical development flow.

## MVP Goal:
Deliver a functional platform enabling seekers to find, book, have a session with, pay, and rate consultants, validating the core value proposition and transaction loop.

## Iterations:

**Iteration 1: Backend Foundation & Core Models**
*   **Goal:** Set up the backend project, database, and core data structures.
*   **Key Activities:** Initialize FastAPI project, configure database (PostgreSQL), define User, Profile, Availability, Booking, Payment, Rating models (SQLAlchemy/Pydantic), setup Alembic migrations, implement basic JWT authentication logic (password hashing, token generation/validation).

**Iteration 2: Backend APIs - Profile & Discovery**
*   **Goal:** Expose APIs for managing consultant profiles and allowing seekers to discover them.
*   **Key Activities:** Create CRUD API endpoints for Consultant Profiles (including rate), API endpoints for setting/getting Availability Slots, API endpoint for listing consultants (directory), API endpoint for keyword search, API endpoint for viewing individual profiles. Implement role-based access control.

**Iteration 3: Backend APIs - Booking & Payment Setup**
*   **Goal:** Enable the booking workflow and integrate payment provider setup.
*   **Key Activities:** Create API endpoints for Seekers to request bookings, API endpoints for Consultants to view/accept/decline bookings, integrate Stripe API for saving Seeker payment methods and initiating Consultant Stripe Connect onboarding, implement basic booking status updates and notifications (internal state).

**Iteration 4: Backend APIs - Session & Payment Execution**
*   **Goal:** Handle the session lifecycle, payment capture, payouts, and ratings.
*   **Key Activities:** Create API endpoints to "start" and "end" sessions (updating booking status), implement logic for 10-min window check, integrate Stripe API for payment pre-authorization (on booking confirmation) and capture (on session end > 10 mins), implement logic for commission calculation and triggering Stripe payouts, create API endpoint for submitting ratings.

**Iteration 5: Frontend Foundation & Authentication**
*   **Goal:** Set up the frontend project and implement user authentication UI.
*   **Key Activities:** Initialize React (Vite) project, setup routing, create reusable UI components, build Registration and Login pages/forms, integrate with backend authentication APIs, implement state management for user session, create basic logged-in/logged-out layouts.

**Iteration 6: Frontend - Profile & Discovery**
*   **Goal:** Build the UI for seekers to find consultants and for consultants to manage profiles.
*   **Key Activities:** Build Consultant Directory page (list display, search bar), build Consultant Profile view page (displaying all details, rate, availability), build Consultant Profile Edit page (forms for details, rate, availability management), integrate all views with corresponding backend APIs.

**Iteration 7: Frontend - Booking & Session Flow**
*   **Goal:** Implement the UI for booking, managing bookings, and the basic session interface.
*   **Key Activities:** Implement booking request UI on consultant profile (selecting slots), build dashboard views for Seekers/Consultants to see upcoming/pending/past bookings, create basic "Session" view (participants, start/end buttons, 10-min timer), implement rating submission UI post-session, integrate with backend booking/session/rating APIs.

**Iteration 8: Frontend - Payment Integration**
*   **Goal:** Integrate secure payment UI elements.
*   **Key Activities:** Implement Stripe Elements for Seeker payment method management, implement UI flow for redirecting Consultants to Stripe Connect onboarding, display basic transaction history, integrate with backend payment setup APIs.

## Post-MVP Considerations (Future Iterations):
*   Advanced Search/Filtering
*   Real-time features (chat, notifications, consultant online status)
*   Integrated Video/Audio
*   Detailed Reviews/Testimonials
*   Consultant Promotion Features
*   Admin Panel Enhancements
*   Freemium Features (Recordings, etc.)
*   Calendar Integrations
*   Dispute Resolution Workflow
