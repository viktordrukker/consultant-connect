# Consultant Connect MVP - Atomic Task Breakdown

## Core Value Proposition
AI-powered platform connecting customers with consultants via instant video calls with 10-minute auto-billing threshold.

## MVP Scope (4-6 weeks)

### Phase 1: Backend Foundation (Week 1)
**Authentication & User Management**
- [ ] JWT authentication system with refresh tokens
- [ ] User registration/login endpoints
- [ ] Password hashing with bcrypt
- [ ] Role-based access (customer/consultant)
- [ ] Email verification system

**Database Setup**
- [ ] PostgreSQL connection and session management
- [ ] Alembic migrations for all models
- [ ] Database seeding scripts for testing
- [ ] Connection pooling configuration

**Core Models Implementation**
- [ ] User model with role enum
- [ ] ConsultantProfile with expertise tags (JSON)
- [ ] Question model (customer questions)
- [ ] Session model (video call sessions)
- [ ] Payment model (stripe integration)
- [ ] Rating model (post-session feedback)

### Phase 2: Core Business Logic (Week 2)
**Consultant Management**
- [ ] Profile creation/update API
- [ ] LinkedIn data import simulation
- [ ] Availability status toggle
- [ ] Expertise tags management
- [ ] Hourly rate setting

**Question & Matching Engine**
- [ ] Question posting API
- [ ] Simple keyword matching algorithm
- [ ] Consultant availability check
- [ ] Match scoring based on tags + availability + ratings
- [ ] Real-time notifications for matches

**Session Management**
- [ ] Session creation on match acceptance
- [ ] Video call room generation (WebRTC or Zoom API)
- [ ] 10-minute timer implementation
- [ ] Session status tracking (pending/active/completed)
- [ ] Auto-billing trigger after 10 minutes

### Phase 3: Payment Integration (Week 2-3)
**Stripe Integration**
- [ ] Stripe customer creation
- [ ] Payment method storage
- [ ] Consultant Connect accounts (for payouts)
- [ ] Session pre-authorization
- [ ] Auto-charge after 10 minutes
- [ ] Commission calculation (15%)
- [ ] Payout automation

**Billing Logic**
- [ ] Session duration tracking
- [ ] Pricing calculation based on consultant rates
- [ ] Refund logic for <10 minute sessions
- [ ] Invoice generation
- [ ] Dispute handling endpoints

### Phase 4: Frontend Application (Week 3-4)
**Core UI Structure**
- [ ] React + Vite setup with TypeScript
- [ ] Authentication pages (login/register)
- [ ] Layout with navigation
- [ ] Responsive design system
- [ ] Error handling and loading states

**Customer Flow**
- [ ] Question posting form
- [ ] Available consultants display
- [ ] Consultant profile preview
- [ ] Video call interface
- [ ] Session timer display
- [ ] Payment confirmation
- [ ] Rating/feedback form

**Consultant Dashboard**
- [ ] Profile management form
- [ ] Incoming question notifications
- [ ] Accept/decline question interface
- [ ] Earnings dashboard
- [ ] Session history
- [ ] Performance metrics

### Phase 5: Video Integration (Week 4)
**WebRTC Implementation**
- [ ] Peer-to-peer video call setup
- [ ] Screen sharing capability
- [ ] Chat functionality during calls
- [ ] Call quality monitoring
- [ ] Recording capability (optional)

**Call Management**
- [ ] Room creation and joining
- [ ] Participant management
- [ ] Connection quality indicators
- [ ] Auto-disconnect after session ends
- [ ] Call history storage

### Phase 6: AI & Automation (Week 5-6)
**Matching Algorithm**
- [ ] Keyword extraction from questions
- [ ] Consultant expertise scoring
- [ ] Availability weighting
- [ ] Rating-based ranking
- [ ] Response time tracking
- [ ] Success rate learning

**Quality Control**
- [ ] Trust score calculation
- [ ] Automatic flagging system
- [ ] Performance analytics
- [ ] Abuse detection
- [ ] Review moderation

## Success Metrics
- **Customer:** Question to call connection < 2 minutes
- **Consultant:** 80%+ utilization of available time
- **Platform:** 95%+ session completion rate
- **Revenue:** 15% commission on all paid sessions

## Technical Constraints
- **Budget:** Use free tiers (PostgreSQL, Redis, WebRTC)
- **Performance:** Sub-second API response times
- **Scale:** Handle 100 concurrent sessions
- **Security:** GDPR compliant data handling

## Out of Scope (Post-MVP)
- Mobile apps
- Advanced scheduling/calendar integration
- Multi-language support
- Advanced analytics dashboard
- White-label solutions
