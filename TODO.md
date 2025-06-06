# Consultant Connect - Development Tasks

## Current Status: Business Case Complete & Ready for Development ✅

### Completed ✅
- [x] Repository cleanup (removed complex docs, outdated models)
- [x] Updated database models for AI-driven approach
- [x] Created simplified Question → Match → Session → Rating flow
- [x] Enhanced README with clear vision and MVP roadmap
- [x] Defined atomic task breakdown in SCOPE.md
- [x] **BUSINESS_CASE.md created** - Comprehensive investor pitch with unit economics
- [x] Progressive commission structure designed (5-20% based on performance)
- [x] Rookie consultant support program defined
- [x] 5-year financial projections with $500K seed → $50M exit path

### Business Fundamentals Locked In ✅
- **Commission Model**: 15% standard, 8% for experts, 20% for rookies (with support)
- **Unit Economics**: 10.7% platform margin at $50 sessions, 4.2% at $100 sessions
- **Market Size**: $50B TAM, targeting $50M SOM (0.1% market share)
- **Technology Costs**: $0.12 per session (Daily.co WebRTC + infrastructure)
- **Break-even**: 300 sessions/month to cover $3K base costs

### Immediate Next Steps (Week 1)

#### Backend Foundation Priority Tasks

**1. Dependencies & Environment Setup**
- [ ] Add missing packages to requirements.txt (JWT, password hashing, etc.)
- [ ] Create .env.example file
- [ ] Setup database connection and session management
- [ ] Configure Alembic for our new models

**2. Authentication System**
- [ ] Install python-jose[cryptography], passlib[bcrypt]
- [ ] Create auth utilities (password hashing, JWT tokens)
- [ ] Build auth endpoints (register, login, refresh token)
- [ ] Add role-based access control middleware

**3. Database Setup**
- [ ] Generate Alembic migration for all models
- [ ] Create database seeding script with sample data
- [ ] Test all model relationships work correctly
- [ ] Add database health check endpoint
- [ ] Add consultant tier fields to support progressive commission model

**4. Core API Structure**
- [ ] Create FastAPI router structure
- [ ] Add Pydantic schemas for request/response validation
- [ ] Implement error handling middleware
- [ ] Add CORS and security headers

### Enhanced Development Strategy (Post-Business Case)

**Small Iterations Approach:**
1. **Authentication + Models + Tiers** (2-3 days)
2. **Question Management APIs** (1-2 days) 
3. **Basic AI Matching Logic** (2-3 days)
4. **Session Management + Billing Logic** (2-3 days)

**Business Logic Integration:**
- Commission calculation based on consultant tier
- Rookie support features (profile guidance, question filtering)
- Session duration tracking for 10-minute billing threshold
- Trust score calculation for AI matching

### Key Files to Create Next

```
backend/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py              # Dependencies (auth, db)
│   │   ├── auth.py              # Authentication endpoints
│   │   ├── users.py             # User management
│   │   ├── questions.py         # Question posting/browsing
│   │   ├── consultants.py       # Consultant profiles + tiers
│   │   ├── sessions.py          # Session management + billing
│   │   └── matching.py          # AI matching endpoints
│   ├── core/
│   │   ├── security.py          # Password hashing, JWT
│   │   ├── database.py          # DB session management
│   │   └── billing.py           # Commission calculation logic
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py              # Auth request/response models
│   │   ├── user.py              # User schemas
│   │   ├── question.py          # Question schemas
│   │   ├── session.py           # Session schemas
│   │   └── consultant.py        # Consultant profile + tier schemas
│   └── services/
│       ├── __init__.py
│       ├── matching.py          # AI matching logic
│       ├── notifications.py     # Real-time notifications
│       ├── billing.py           # Stripe integration + commission calc
│       └── tiers.py             # Consultant tier management
├── alembic/
│   └── versions/
│       └── 001_initial_migration.py
└── .env.example
```

### Success Criteria for Week 1
- [ ] All models migrate successfully with tier support
- [ ] Authentication endpoints work (register/login)
- [ ] Can create users and consultant profiles with tier assignment
- [ ] Database seeds with test data including different consultant tiers
- [ ] Commission calculation logic implemented and tested
- [ ] API documentation auto-generated
- [ ] Health check endpoints respond

### Critical Business Decisions Implemented
1. **Progressive Commission Structure**: 15% → 8% as consultants grow
2. **Rookie Support Program**: Built-in guidance, question filtering
3. **10-Minute Billing Threshold**: Free trial, then auto-billing
4. **AI-First Matching**: Keyword extraction + consultant scoring
5. **WebRTC First**: Daily.co for MVP, Zoom API for scale

### Investment-Ready Metrics to Track
- **GMV per session**: Target $200-500 range
- **Session completion rate**: Target 95%+
- **Consultant tier progression**: 70% rookie → growing conversion
- **Customer satisfaction**: 4.2+ average rating
- **Platform margin**: 4-11% depending on consultant tier

### Risk Mitigation
- **Scope Creep**: Stick to atomic tasks, resist feature additions
- **Over-Engineering**: Build minimum viable features first
- **Technical Debt**: Document trade-offs, plan refactoring
- **Dependencies**: Keep minimal, prefer standard libraries
- **Unit Economics**: Monitor commission vs. costs closely

### Next Major Milestones
- **Month 3**: 200 consultants, 50 sessions/month
- **Month 6**: 500 consultants, 300 sessions/month, $15K MRR
- **Month 12**: 1K consultants, 800 sessions/month, $50K MRR
- **Month 18**: Series A fundraising at $600K ARR run rate

---
**Next Update**: After completing Week 1 authentication + models + tier system implementation
