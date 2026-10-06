<footer id="contact">
  <div class="container footer-grid">
    <div class="intro">
      <div class="crest">QT</div>
      <h2>Queen Tovah Cares Foundation International</h2>
      <p>
        Compassion with dignity. Opportunity with purpose. A global outlook rooted in service to
        people and communities.
      </p>
    </div>

    <div class="links">
      <p class="label">Explore</p>
      <a href="#about">About the Foundation</a>
      <a href="#programs">Our Programs</a>
      <a href="#founder">Founder</a>
      <a href="#impact">Our Approach</a>
    </div>

    <div class="links">
      <p class="label">Connect</p>
      <a href="mailto:info@queentovah.org">info@queentovah.org</a>
      <span>Partnerships & humanitarian enquiries</span>
      <span>Scholarships & community programs</span>
    </div>
  </div>

  <div class="container bottom">
    <span>© {new Date().getFullYear()} Queen Tovah Cares Foundation International.</span>
    <em>“It is good to be good.”</em>
  </div>
</footer>

<style>
  footer {
    position: relative;
    overflow: hidden;
    border-top: 1px solid rgba(225, 189, 106, 0.16);
    padding: 76px 0 26px;
    background:
      radial-gradient(circle at 90% 20%, rgba(100, 25, 111, 0.22), transparent 26rem),
      #070307;
  }

  .footer-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.6fr) 0.8fr 1fr;
    gap: 54px;
  }

  .crest {
    display: grid;
    width: 54px;
    height: 54px;
    place-items: center;
    border: 1px solid rgba(225, 189, 106, 0.48);
    border-radius: 50%;
    color: var(--gold-bright);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 700;
  }

  h2 {
    max-width: 500px;
    margin: 20px 0 12px;
    font-family: 'Cormorant Garamond', Georgia, serif;
    color: var(--champagne);
    font-size: clamp(1.9rem, 3vw, 2.8rem);
    font-weight: 600;
    line-height: 1;
  }

  .intro p,
  .links span {
    color: #a998a8;
  }

  .intro p {
    max-width: 540px;
    margin: 0;
  }

  .links {
    display: flex;
    flex-direction: column;
    gap: 11px;
    font-size: 0.9rem;
  }

  .label {
    margin: 0 0 6px;
    color: var(--gold-bright);
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .links a {
    color: #e5dbe4;
  }

  .links a:hover {
    color: var(--gold-bright);
  }

  .bottom {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-top: 58px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 24px;
    color: #8f7f8e;
    font-size: 0.82rem;
  }

  .bottom em {
    color: var(--gold-bright);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1rem;
  }

  @media (max-width: 800px) {
    .footer-grid {
      grid-template-columns: 1fr 1fr;
    }

    .intro {
      grid-column: 1 / -1;
    }
  }

  @media (max-width: 560px) {
    .footer-grid {
      grid-template-columns: 1fr;
    }

    .intro {
      grid-column: auto;
    }

    .bottom {
      flex-direction: column;
    }
  }
</style>
