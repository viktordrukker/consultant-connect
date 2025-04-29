# Value Creation Flow

This diagram illustrates how value (expertise, leads, money, reputation, etc.) is exchanged between the Expert Seekers, the Consultants, and the Consultant Connect Platform.

```mermaid
graph TD
    subgraph Actors
        Seeker[Expert Seeker <br/> (e.g., Sarah)]
        Platform[Consultant Connect Platform]
        Consultant[Consultant <br/> (e.g., Alex)]
    end

    subgraph "Value Exchange: Seeker <--> Platform"
        Seeker -- Payment for Sessions --> Platform
        Platform -- Access to Vetted Consultants <br/> Connection Facilitation <br/> Trust & Security <br/> Value-Add Features (Optional) --> Seeker
    end

    subgraph "Value Exchange: Consultant <--> Platform"
        Consultant -- Commission Fees <br/> Promotion Fees (Optional) --> Platform
        Platform -- Qualified Leads <br/> Profile Hosting & Visibility <br/> Reputation Management <br/> Scheduling & Payment Tools <br/> Payment Guarantee --> Consultant
    end

    subgraph "Value Exchange: Seeker <--> Consultant (via Platform)"
        Seeker -- Need for Expertise <br/> Session Payment (via Platform) --> Consultant
        Consultant -- Expert Advice & Solutions <br/> Session Delivery --> Seeker
    end

    style Seeker fill:#ccf,stroke:#333,stroke-width:2px
    style Consultant fill:#cfc,stroke:#333,stroke-width:2px
    style Platform fill:#fcc,stroke:#333,stroke-width:2px
```

**Explanation of Key Value Flows:**

1.  **Seeker to Platform:** Seekers provide monetary value by paying for successful consulting sessions.
2.  **Platform to Seeker:** The platform provides value by offering a curated pool of consultants, facilitating easy connection and scheduling, ensuring a level of trust (through profiles, reviews, payment handling), and potentially offering premium features (like recordings).
3.  **Consultant to Platform:** Consultants provide monetary value through commissions on their earnings and optional fees for premium placement/promotion. They also contribute content (profiles, expertise) which is core to the platform's offering.
4.  **Platform to Consultant:** The platform delivers value by providing access to potential clients (leads), tools to manage their online presence and reputation, administrative support (scheduling, payment processing), and the security of guaranteed payment for completed work.
5.  **Seeker to Consultant:** The seeker brings their specific need/problem and the payment for the consultant's time/expertise (facilitated securely by the platform).
6.  **Consultant to Seeker:** The consultant provides their core value – expert knowledge, advice, and solutions delivered during the session.
