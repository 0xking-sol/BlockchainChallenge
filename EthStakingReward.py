# a
# What would be the estimated APR for staking ETH if the staking ratio of ETH goes from
# 15% to 50%?

def calculate_apr(staked_eth_percentage):
    base_reward_factor = 64
    max_issuance = 2_097_152
    total_eth = 119_370_000  # Total supply of ETH as of Tuesday 18th April

    # Adjust total_eth for the staking ratio
    staked_eth = total_eth * staked_eth_percentage
    non_staked_eth = total_eth - staked_eth

    reward = (max_issuance * base_reward_factor) / (staked_eth ** 0.5)
    annual_reward = reward * 60 * 60 * 24 * 365  # 1 reward per epoch (12s)
    annual_reward_percentage = (annual_reward / non_staked_eth) * 100

    return annual_reward_percentage

# Calculate the APR for 15% and 50% staking ratio
apr_15 = calculate_apr(0.15)
apr_50 = calculate_apr(0.50)

print(f"Estimated APR for 15% staking ratio: {apr_15:.2f}%")
print(f"Estimated APR for 50% staking ratio: {apr_50:.2f}%")
