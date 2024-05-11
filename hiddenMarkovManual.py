def estimate_weather(observations):
    # Initial probabilities for Rainy (R) and Sunny (S)
    initial_probs = {'R': 0.6, 'S': 0.4}

    # Transition probabilities P(X_t | X_{t-1})
    transition_probs = {
        'R': {'R': 0.7, 'S': 0.3},
        'S': {'R': 0.4, 'S': 0.6}
    }

    # Probability of observations given state P(E_t | X_t)
    emission_probs = {
        'R': {'W': 0.1, 'Sh': 0.4, 'C': 0.5},
        'S': {'W': 0.6, 'Sh': 0.3, 'C': 0.1}
    }

    # Initialize the posterior probability as the initial probability
    posterior = initial_probs.copy()

    for obs in observations:
        new_posterior = {}
        for current_state in ['R', 'S']:
            # Calculate total probability for the current state
            total_prob = 0
            for previous_state in ['R', 'S']:
                # P(X_t = current_state | X_{t-1} = previous_state) * P(X_{t-1} = previous_state)
                total_prob += transition_probs[previous_state][current_state] * \
                    posterior[previous_state]

            # Update the posterior probability for the current state
            # P(E_t = obs | X_t = current_state) * total probability for the state
            new_posterior[current_state] = emission_probs[current_state][obs] * total_prob

        # Normalize the new posterior to sum to 1
        normalization_factor = sum(new_posterior.values())
        for state in new_posterior:
            new_posterior[state] /= normalization_factor

        posterior = new_posterior

        print("The probability distribution of the weather given the observation",
              obs, "is:", posterior)

    return posterior


# Test the function with the sequence of observations 'Sh' followed by 'C'
observations = ['Sh', 'C']
result = estimate_weather(observations)
